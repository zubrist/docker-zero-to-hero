from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import redis
import json

app = FastAPI(title="Interactive Visitor Counter")
redis_client = redis.Redis(host='redis', port=6379)

class Score(BaseModel):
    username: str
    score: int
    mode: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    visits = str(redis_client.incr('visits')).zfill(7)  # Pad with zeros to 7 digits
    
    # Generate HTML for each digit
    digits_html = ''.join([f'<div class="digit">{d}</div>' for d in visits])
    
    # Get top 5 scores for each mode
    modes = ['10sec', '30sec', '60sec']
    all_scores = {}
    for mode in modes:
        all_scores[mode] = get_top_scores(mode)
    
    scores_html = ""
    for mode in modes:
        scores_html += f'''
        <div class="mode-scores">
            <h3>{mode.upper()} Mode</h3>
            <ul>
                {"".join([f"<li style='color: var(--accent);'>{score['username']}: {score['score']}</li>" for score in all_scores[mode]])}
            </ul>
        </div>
        '''

    return f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>The Obvious Clicker Game</title>
            <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
            <style>
                @font-face {{
                    font-family: 'Origin Tech';
                    src: url('https://fonts.cdnfonts.com/css/origin-tech-demo') format('woff2');
                }}
                
                :root {{
                    --bg-primary: #0a192f;
                    --bg-secondary: #112240;
                    --text-primary: #64ffda;
                    --text-secondary: #8892b0;
                    --accent: #00ff00;
                    --danger: #ff3864;
                }}

                body {{
                    font-family: 'Share Tech Mono', monospace;
                    background-color: var(--bg-primary);
                    color: var(--text-primary);
                    max-width: 900px;
                    margin: 0 auto;
                    padding: 20px;
                    text-align: center;
                }}

                .counter {{
                    display: flex;
                    gap: 10px;
                    justify-content: center;
                    margin: 20px 0;
                }}

                .digit {{
                    background: #1a1a1a;
                    color: #ffffff;
                    font-family: 'Share Tech Mono', monospace;
                    font-size: 48px;
                    width: 60px;
                    height: 80px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    border-radius: 8px;
                    position: relative;
                    box-shadow: 0 0 10px rgba(100, 255, 218, 0.2);
                    border: 1px solid rgba(100, 255, 218, 0.1);
                }}

                .digit::after {{
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    border-radius: 8px;
                    box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.5);
                    pointer-events: none;
                }}

                .digit::before {{
                    content: '';
                    position: absolute;
                    top: 1px;
                    left: 1px;
                    right: 1px;
                    height: 50%;
                    background: linear-gradient(to bottom, 
                        rgba(255, 255, 255, 0.1) 0%,
                        rgba(255, 255, 255, 0) 100%);
                    border-radius: 8px 8px 0 0;
                    pointer-events: none;
                }}

                @keyframes digitChange {{
                    0% {{ transform: translateY(-2px); opacity: 0.5; }}
                    100% {{ transform: translateY(0); opacity: 1; }}
                }}

                .digit {{
                    animation: digitChange 0.3s ease-out;
                }}

                .game-container {{
                    background: var(--bg-secondary);
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 20px rgba(100, 255, 218, 0.1);
                    margin: 20px 0;
                    border: 1px solid var(--text-primary);
                }}

                .button {{
                    background-color: transparent;
                    color: var(--text-primary);
                    padding: 10px 20px;
                    border: 2px solid var(--text-primary);
                    border-radius: 5px;
                    cursor: pointer;
                    margin: 5px;
                    font-family: 'Share Tech Mono', monospace;
                    transition: all 0.3s ease;
                }}

                .button:hover {{
                    background-color: var(--text-primary);
                    color: var(--bg-primary);
                    box-shadow: 0 0 15px var(--text-primary);
                    transform: translateY(-2px);
                }}

                .leaderboard {{
                    background: var(--bg-secondary);
                    padding: 20px;
                    border-radius: 10px;
                    margin-top: 20px;
                    border: 1px solid var(--text-primary);
                    display: flex;
                    justify-content: space-around;
                    
                }}

                .mode-scores {{
                    flex: 1;
                    margin: 0 10px;
                }}

                .score {{
                    font-size: 24px;
                    color: var(--accent);
                }}

                .mode-select {{
                    margin: 20px 0;
                }}

                input {{
                    background: var(--bg-secondary);
                    border: 1px solid var(--text-primary);
                    color: var(--text-primary);
                    padding: 8px;
                    border-radius: 5px;
                    font-family: 'Share Tech Mono', monospace;
                }}

                .click-effect {{
                    position: absolute;
                    pointer-events: none;
                    animation: clickRipple 0.5s ease-out;
                }}

                @keyframes pulse {{
                    0% {{ opacity: 1; }}
                    50% {{ opacity: 0.8; }}
                    100% {{ opacity: 1; }}
                }}

                @keyframes clickRipple {{
                    0% {{
                        transform: scale(0);
                        opacity: 1;
                    }}
                    100% {{
                        transform: scale(1);
                        opacity: 0;
                    }}
                }}

                .click-button {{
                    background-color: #00ff88;
                    color: #0a192f;
                    width: 150px;
                    height: 150px;
                    border-radius: 50%;
                    border: 3px solid #00ff88;
                    font-weight: bold;
                    font-size: 1.2em;
                    text-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
                    box-shadow: 0 0 20px rgba(0, 255, 136, 0.4);
                    transition: all 0.3s ease;
                    animation: pulse 2s infinite;
                }}

                .click-button:hover {{
                    transform: scale(1.1);
                    box-shadow: 0 0 30px rgba(0, 255, 136, 0.6);
                    background-color: #00ff99;
                }}

                .click-button:active {{
                    transform: scale(0.95);
                    background-color: #00cc77;
                }}

                @keyframes pulse {{
                    0% {{
                        box-shadow: 0 0 20px rgba(0, 255, 136, 0.4);
                    }}
                    50% {{
                        box-shadow: 0 0 30px rgba(0, 255, 136, 0.6);
                    }}
                    100% {{
                        box-shadow: 0 0 20px rgba(0, 255, 136, 0.4);
                    }}
                }}

                /* Make other buttons stand out less */
                .button:not(.click-button) {{
                    opacity: 0.8;
                }}
            </style>
        </head>
        <body>
            <h1>THE OBVIOUS CLICKER GAME</h1>
            <p>Total Visits:</p>
            <div class="counter">
                {digits_html}
            </div>

            <div class="game-container">
                <h2>SPEED CLICKING CHALLENGE</h2>
                <div class="mode-select">
                    <button class="button mode-btn" data-mode="10">10 SEC</button>
                    <button class="button mode-btn" data-mode="30">30 SEC</button>
                    <button class="button mode-btn" data-mode="60">60 SEC</button>
                </div>
                <p>Mode: <span id="currentMode">10 SEC</span></p>
                <p>Score: <span id="score" class="score">0</span></p>
                <p>Time Left: <span id="timer">10</span>s</p>
                <button id="clickBtn" class="button click-button">CLICK ME 🎯</button>
                <button id="resetBtn" class="button">RESET</button>
                <input type="text" id="username" placeholder="ENTER CODENAME">
                <button id="saveScore" class="button">SAVE SCORE</button>
            </div>

            <div class="leaderboard">
                <h2>TOP OPERATORS</h2>
                {scores_html}
            </div>

            <audio id="clickSound" src="https://www.soundjay.com/button/button-09a.mp3" preload="auto"></audio>
            <audio id="gameOverSound" src="https://www.soundjay.com/button/button-21.mp3" preload="auto"></audio>

            <script>
                let score = 0;
                let timeLeft = 10;
                let gameActive = false;
                let timer;
                let currentMode = 10;
                const clickSound = document.getElementById('clickSound');
                const gameOverSound = document.getElementById('gameOverSound');

                // Click effect
                document.addEventListener('click', (e) => {{
                    const effect = document.createElement('div');
                    effect.className = 'click-effect';
                    effect.style.left = e.clientX + 'px';
                    effect.style.top = e.clientY + 'px';
                    effect.style.border = '2px solid var(--accent)';
                    effect.style.width = '20px';
                    effect.style.height = '20px';
                    effect.style.borderRadius = '50%';
                    document.body.appendChild(effect);
                    setTimeout(() => effect.remove(), 500);
                }});

                // Mode selection
                document.querySelectorAll('.mode-btn').forEach(btn => {{
                    btn.addEventListener('click', () => {{
                        currentMode = parseInt(btn.dataset.mode);
                        document.getElementById('currentMode').textContent = currentMode + ' SEC';
                        resetGame();
                    }});
                }});

                document.getElementById('clickBtn').addEventListener('click', () => {{
                    clickSound.currentTime = 0;
                    clickSound.play();
                    if (!gameActive) {{
                        startGame();
                    }}
                    score++;
                    document.getElementById('score').textContent = score;
                }});

                document.getElementById('resetBtn').addEventListener('click', resetGame);

                document.getElementById('saveScore').addEventListener('click', async () => {{
                    const username = document.getElementById('username').value;
                    if (!username) {{
                        alert('Please enter a codename!');
                        return;
                    }}
                    
                    try {{
                        const response = await fetch('/api/scores', {{
                            method: 'POST',
                            headers: {{
                                'Content-Type': 'application/json',
                            }},
                            body: JSON.stringify({{
                                username: username,
                                score: score,
                                mode: currentMode + 'sec'
                            }})
                        }});
                        const data = await response.json();
                        location.reload();
                    }} catch (error) {{
                        console.error('Error:', error);
                    }}
                }});

                function startGame() {{
                    gameActive = true;
                    timeLeft = currentMode;
                    score = 0;
                    document.getElementById('score').textContent = score;
                    
                    timer = setInterval(() => {{
                        timeLeft--;
                        document.getElementById('timer').textContent = timeLeft;
                        
                        if (timeLeft <= 0) {{
                            endGame();
                        }}
                    }}, 1000);
                }}

                function endGame() {{
                    gameActive = false;
                    clearInterval(timer);
                    gameOverSound.play();
                    alert(`SEQUENCE COMPLETE!\nFinal Score: ${{score}}`);
                }}

                function resetGame() {{
                    gameActive = false;
                    clearInterval(timer);
                    score = 0;
                    timeLeft = currentMode;
                    document.getElementById('score').textContent = score;
                    document.getElementById('timer').textContent = timeLeft;
                }}
            </script>
        </body>
    </html>
    '''

@app.post("/api/scores")
async def save_score(score: Score):
    scores = get_top_scores(score.mode)
    scores.append({"username": score.username, "score": score.score})
    scores.sort(key=lambda x: x["score"], reverse=True)
    scores = scores[:5]  # Keep only top 5
    redis_client.set(f'high_scores_{score.mode}', json.dumps(scores))
    return {"message": "Score saved successfully"}

def get_top_scores(mode):
    scores = redis_client.get(f'high_scores_{mode}')
    if scores:
        return json.loads(scores)
    return []
