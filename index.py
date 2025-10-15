from flask import Flask, redirect
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

link_lists = {
    "discord": "https://discord.gg/pqD6hEj",
    "github": "https://github.com/ba-ka",
    "ws": "https://discord.gg/EsqRxP2",
    "gip-roadmap": "https://trello.com/b/abue61dQ.html",
    "gip": "https://www.roblox.com/games/5253868577/ghost-id-project",
    "ah0": "https://ah0.ba-ka.org/user/baka",
    "mg": "https://www.roblox.com/games/5111122533/maze-games",
    "roblox": "https://www.roblox.com/groups/5346197/ba-ka",
    "steam": "https://steamcommunity.com/groups/ba-ka-org",
}
x_ba_ka = "https://x.ba-ka.org"
port = int(os.getenv("PORT", "3000"))


@app.route("/")
def index():
    return redirect(x_ba_ka)


@app.route("/<name>")
def redir(name: str):
    if name in link_lists.keys():
        return redirect(link_lists[name])

    return redirect(x_ba_ka)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
