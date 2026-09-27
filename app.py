from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    profile = {
        "name": "Your Name",
        "username": "@yourusername",
        "bio": "Welcome to my little corner of the internet 🌐",
        "profile_image": "profile.jpg",
    }

    links = [
        {
            "title": "My Website",
            "url": "https://example.com",
            "icon": "🌐",
        },
        {
            "title": "My YouTube Channel",
            "url": "https://youtube.com",
            "icon": "▶️",
        },
        {
            "title": "Instagram",
            "url": "https://instagram.com",
            "icon": "📸",
        },
        {
            "title": "GitHub",
            "url": "https://github.com",
            "icon": "💻",
        },
        {
            "title": "Contact Me",
            "url": "mailto:you@example.com",
            "icon": "✉️",
        },
    ]

    social_links = [
        {
            "name": "Instagram",
            "url": "https://instagram.com",
            "icon": "◎",
        },
        {
            "name": "YouTube",
            "url": "https://youtube.com",
            "icon": "▶",
        },
        {
            "name": "GitHub",
            "url": "https://github.com",
            "icon": "⌘",
        },
        {
            "name": "Twitter",
            "url": "https://x.com",
            "icon": "𝕏",
        },
    ]

    return render_template(
        "index.html",
        profile=profile,
        links=links,
        social_links=social_links,
    )


if __name__ == "__main__":
    app.run(debug=True)
