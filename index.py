from flask import Flask, redirect
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return redirect("https://x.ba-ka.org")

@app.route('/<name>')
def redir(name):
    if name == "discord":
        return redirect("https://discord.gg/pqD6hEj")
    
    if name == "github":
        return redirect("https://github.com/ba-ka")

    if name == "ws":
        return redirect("https://discord.gg/EsqRxP2")

    if name == "gip-roadmap	":
        return redirect("https://trello.com/b/abue61dQ.html")

    if name == "gip":
        return redirect("https://www.roblox.com/games/5253868577/ghost-id-project")

    if name == "ah0":
        return redirect("https://ah0.ba-ka.org/user/baka")

    if name == "mg":
        return redirect("https://www.roblox.com/games/5111122533/maze-games")

    if name == "roblox":
        return redirect("https://www.roblox.com/groups/5346197/ba-ka")

    if name == "steam":
        return redirect("https://steamcommunity.com/groups/ba-ka-org")

    return redirect("https://x.ba-ka.org")
