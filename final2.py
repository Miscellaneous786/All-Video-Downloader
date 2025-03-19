import gradio as gr
import yt_dlp

def get_video_url(url):
    try:
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'noplaylist': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get("url", None)
            
            if video_url:
                # Append &dl=1 to force download (works for many sources)
                download_url = video_url + "&dl=1"
                return download_url, f'<a href="{download_url}" download target="_blank">Click Here to Download</a>'
            else:
                return None, "Could not retrieve the video URL."
    
    except Exception as e:
        return None, f"Error: {str(e)}"

app = gr.Interface(
    fn=get_video_url,
    inputs=gr.Textbox(label="Enter Video URL"),
    outputs=[
        gr.Textbox(label="Direct Download URL"),  # Hidden raw URL (for debugging)
        gr.HTML(label="Download Link")  # Clickable download link
    ],
    title="Universal Video Downloader",
    description="Paste a video URL from YouTube, Instagram, or Facebook and get a direct MP4 download link.",
    theme="compact",
)

app.launch(share=True)
