from flask import Flask, render_template, request, send_file, Response
from curl_cffi import requests
import io
import urllib.parse

app = Flask(__name__)

# --- Helper Function: Fetch Profile Data ---
def fetch_insta_data(username):
    url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
    headers = {
        "X-IG-App-ID": "936619743392459",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        # Impersonate chrome to bypass TLS fingerprinting
        response = requests.get(url, headers=headers, impersonate="chrome110")
        
        if response.status_code != 200:
            return "error_rate_limited" if response.status_code == 429 else "error_not_found"

        data = response.json()["data"]["user"]
        
        profile_data = {
            "username": data["username"],
            "full_name": data["full_name"],
            "bio": data["biography"],
            "followers": f"{data['edge_followed_by']['count']:,}",
            "following": f"{data['edge_follow']['count']:,}",
            "posts_count": data["edge_owner_to_timeline_media"]["count"],
            "profile_pic": data["profile_pic_url_hd"],
            "external_url": data.get("external_url"),
            "posts": []
        }

        edges = data["edge_owner_to_timeline_media"]["edges"]
        for edge in edges:
            node = edge["node"]
            
            if "edge_sidecar_to_children" in node:
                child_edges = node["edge_sidecar_to_children"]["edges"]
                for i, child in enumerate(child_edges):
                    child_node = child["node"]
                    media_url = child_node["video_url"] if child_node["is_video"] else child_node["display_url"]
                    
                    profile_data["posts"].append({
                        "url": media_url,
                        "likes": node["edge_liked_by"]["count"],
                        "comments": node["edge_media_to_comment"]["count"],
                        "shortcode": f"{node['shortcode']}_{i}", # Unique shortcode for each slide
                        "is_video": child_node["is_video"]
                    })
            else:
                # Single Post (Image or Video)
                media_url = node["video_url"] if node["is_video"] else node["display_url"]
                profile_data["posts"].append({
                    "url": media_url,
                    "likes": node["edge_liked_by"]["count"],
                    "comments": node["edge_media_to_comment"]["count"],
                    "shortcode": node["shortcode"],
                    "is_video": node["is_video"]
                })
            
        return profile_data

    except Exception as e:
        print(f"Fetch Error: {e}")
        return "error_generic"

# --- Route 1: Main Page ---
@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        username = request.form.get('username').strip()
        data = fetch_insta_data(username)
    return render_template('index.html', data=data)

# --- Route 2: Media Proxy (Fixes Broken Images/CORS) ---
@app.route('/proxy-media')
def proxy_media():
    target_url = request.args.get('url')
    if not target_url:
        return "No URL provided", 400
    
    headers = {
        "User-Agent": "Mozilla/5.0",
        "X-IG-App-ID": "936619743392459"
    }
    
    try:
        res = requests.get(target_url, headers=headers, impersonate="chrome110")
        return Response(res.content, mimetype=res.headers.get('Content-Type'))
    except Exception as e:
        return str(e), 500

# --- Route 3: Media Downloader ---
@app.route('/download/<shortcode>')
def download_media(shortcode):
    media_url = request.args.get('url')
    if not media_url:
        return "Invalid Download Request", 400
    
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        res = requests.get(media_url, headers=headers, impersonate="chrome110")
        
        # Determine extension based on content type
        content_type = res.headers.get('Content-Type', '')
        ext = ".mp4" if "video" in content_type else ".jpg"
        filename = f"FirewallLab_{shortcode}{ext}"
            
        return send_file(
            io.BytesIO(res.content),
            mimetype=content_type,
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return f"Download Failed: {e}", 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)