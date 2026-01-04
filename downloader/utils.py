import instaloader


def get_reel_download_url(post_url):
    
    if not post_url or not post_url.strip():
        return None

    L = instaloader.Instaloader()
    try:
        # Extract shortcode from URL (e.g., https://www.instagram.com/reels/C12345/ -> C12345)
        shortcode = post_url.split("/")[-2]
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        
        if post.is_video:
            return post.video_url
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None