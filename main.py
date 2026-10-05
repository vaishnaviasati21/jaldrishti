import tkinter as tk
import random
from datetime import datetime

# =========================================================
# JALDRISHTI - SMART WATER & AGRICULTURAL MONITORING
# =========================================================

root = tk.Tk()
root.title("JalDrishti | Smart Water Monitoring")
root.geometry("1100x720")
root.configure(bg="#07111F")
root.resizable(False, False)

# =========================================================
# COLORS
# =========================================================

BG = "#07111F"
CARD = "#0E1D31"
CARD2 = "#122640"
BORDER = "#1C3552"

TEXT = "#F4F7FB"
MUTED = "#8298B2"

BLUE = "#20C7F3"
GREEN = "#35D399"
YELLOW = "#F5C451"
RED = "#FF5C6C"
PURPLE = "#9B8CFF"

# =========================================================
# DATA
# =========================================================

sensor_data = {
    "moisture": 55,
    "rainfall": 20,
    "water": 50,
    "humidity": 65
}

history = {
    "moisture": [],
    "water": [],
    "rainfall": []
}

MAX_HISTORY = 25

# =========================================================
# HELPER FUNCTIONS
# =========================================================

def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def create_card(parent, title, icon, unit):
    card = tk.Frame(
        parent,
        bg=CARD,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    tk.Label(
        card,
        text=icon,
        font=("Segoe UI Emoji", 20),
        bg=CARD,
        fg=BLUE
    ).pack(anchor="w", padx=18, pady=(12, 0))

    tk.Label(
        card,
        text=title.upper(),
        font=("Segoe UI", 9, "bold"),
        bg=CARD,
        fg=MUTED
    ).pack(anchor="w", padx=18)

    value_label = tk.Label(
        card,
        text="--",
        font=("Segoe UI", 23, "bold"),
        bg=CARD,
        fg=TEXT
    )
    value_label.pack(anchor="w", padx=18, pady=(2, 0))

    unit_label = tk.Label(
        card,
        text=unit,
        font=("Segoe UI", 9),
        bg=CARD,
        fg=MUTED
    )
    unit_label.pack(anchor="w", padx=18, pady=(0, 10))

    return card, value_label


# =========================================================
# HEADER
# =========================================================

header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=35, pady=(25, 5))

left_header = tk.Frame(header, bg=BG)
left_header.pack(side="left")

tk.Label(
    left_header,
    text="🌱 JalDrishti",
    font=("Segoe UI", 28, "bold"),
    bg=BG,
    fg=TEXT
).pack(anchor="w")

tk.Label(
    left_header,
    text="Smart Water & Agricultural Monitoring System",
    font=("Segoe UI", 10),
    bg=BG,
    fg=MUTED
).pack(anchor="w", pady=(2, 0))

# Live status

status_frame = tk.Frame(header, bg=BG)
status_frame.pack(side="right", pady=15)

tk.Label(
    status_frame,
    text="●",
    font=("Segoe UI", 13),
    bg=BG,
    fg=GREEN
).pack(side="left")

status_label = tk.Label(
    status_frame,
    text=" SYSTEM ONLINE",
    font=("Segoe UI", 10, "bold"),
    bg=BG,
    fg=GREEN
)
status_label.pack(side="left")

# =========================================================
# TOP INFORMATION BAR
# =========================================================

info_bar = tk.Frame(
    root,
    bg=CARD2,
    highlightbackground=BORDER,
    highlightthickness=1
)
info_bar.pack(fill="x", padx=35, pady=(15, 18))

info_left = tk.Label(
    info_bar,
    text="●  ESP32 SIMULATION ACTIVE",
    font=("Segoe UI", 9, "bold"),
    bg=CARD2,
    fg=BLUE
)
info_left.pack(side="left", padx=18, pady=10)

time_label = tk.Label(
    info_bar,
    text="",
    font=("Segoe UI", 9),
    bg=CARD2,
    fg=MUTED
)
time_label.pack(side="right", padx=18)


def update_time():
    time_label.config(
        text=datetime.now().strftime("%d %b %Y  •  %I:%M:%S %p")
    )
    root.after(1000, update_time)


update_time()

# =========================================================
# SENSOR CARDS
# =========================================================

cards_frame = tk.Frame(root, bg=BG)
cards_frame.pack(fill="x", padx=35)

moisture_card, moisture_label = create_card(
    cards_frame, "Soil Moisture", "💧", "Moisture level"
)

rainfall_card, rainfall_label = create_card(
    cards_frame, "Rainfall", "🌧", "Millimetres"
)

water_card, water_label = create_card(
    cards_frame, "Water Level", "🌊", "Reservoir level"
)

humidity_card, humidity_label = create_card(
    cards_frame, "Humidity", "☁", "Relative humidity"
)

for card in [
    moisture_card,
    rainfall_card,
    water_card,
    humidity_card
]:
    card.pack(
        side="left",
        expand=True,
        fill="both",
        padx=5
    )

# =========================================================
# MAIN CONTENT
# =========================================================

main_frame = tk.Frame(root, bg=BG)
main_frame.pack(
    fill="both",
    expand=True,
    padx=35,
    pady=18
)

# =========================================================
# RISK PANEL
# =========================================================

risk_panel = tk.Frame(
    main_frame,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)

risk_panel.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 8)
)

tk.Label(
    risk_panel,
    text="CURRENT RISK ASSESSMENT",
    font=("Segoe UI", 10, "bold"),
    bg=CARD,
    fg=MUTED
).pack(pady=(20, 5))

risk_label = tk.Label(
    risk_panel,
    text="LOW",
    font=("Segoe UI", 36, "bold"),
    bg=CARD,
    fg=GREEN
)
risk_label.pack()

score_label = tk.Label(
    risk_panel,
    text="Risk Score: 0 / 100",
    font=("Segoe UI", 12),
    bg=CARD,
    fg=TEXT
)
score_label.pack()

# Progress bar

progress_bg = tk.Frame(
    risk_panel,
    bg="#20364F",
    width=300,
    height=12
)
progress_bg.pack(pady=15)
progress_bg.pack_propagate(False)

progress = tk.Frame(
    progress_bg,
    bg=GREEN,
    width=0,
    height=12
)
progress.place(x=0, y=0)

risk_reason = tk.Label(
    risk_panel,
    text="Conditions are stable.",
    font=("Segoe UI", 10),
    bg=CARD,
    fg=MUTED,
    wraplength=330,
    justify="center"
)
risk_reason.pack(padx=25, pady=5)

# =========================================================
# TREND PANEL
# =========================================================

trend_panel = tk.Frame(
    main_frame,
    bg=CARD,
    highlightbackground=BORDER,
    highlightthickness=1
)

trend_panel.pack(
    side="right",
    fill="both",
    expand=True,
    padx=(8, 0)
)

tk.Label(
    trend_panel,
    text="LIVE SENSOR TREND",
    font=("Segoe UI", 10, "bold"),
    bg=CARD,
    fg=MUTED
).pack(anchor="w", padx=20, pady=(18, 5))

canvas = tk.Canvas(
    trend_panel,
    width=430,
    height=155,
    bg=CARD,
    highlightthickness=0
)
canvas.pack(padx=15, pady=5)

# =========================================================
# RECOMMENDATION
# =========================================================

recommendation = tk.Frame(
    root,
    bg=CARD2,
    highlightbackground=BORDER,
    highlightthickness=1
)
recommendation.pack(
    fill="x",
    padx=35,
    pady=(0, 12)
)

tk.Label(
    recommendation,
    text="🤖 AI RECOMMENDATION",
    font=("Segoe UI", 10, "bold"),
    bg=CARD2,
    fg=BLUE
).pack(side="left", padx=18, pady=12)

message_label = tk.Label(
    recommendation,
    text="Monitoring environmental conditions...",
    font=("Segoe UI", 10),
    bg=CARD2,
    fg=TEXT,
    wraplength=700,
    justify="left"
)
message_label.pack(side="left", padx=10)

# =========================================================
# ALERT LOG
# =========================================================

alert_label = tk.Label(
    root,
    text="✓ No critical alerts",
    font=("Segoe UI", 9),
    bg=BG,
    fg=GREEN
)
alert_label.pack(anchor="w", padx=35)

# =========================================================
# GRAPH
# =========================================================

def draw_graph():

    canvas.delete("all")

    width = 430
    height = 155

    # Grid lines

    for y in range(25, 145, 30):
        canvas.create_line(
            15,
            y,
            width - 10,
            y,
            fill="#1A3048"
        )

    # Draw moisture line

    data = history["moisture"]

    if len(data) < 2:
        return

    points = []

    for i, value in enumerate(data):

        x = 15 + (
            i * (width - 30) /
            max(1, MAX_HISTORY - 1)
        )

        y = 140 - (
            value / 100 * 110
        )

        points.append((x, y))

    for i in range(len(points) - 1):

        canvas.create_line(
            points[i][0],
            points[i][1],
            points[i + 1][0],
            points[i + 1][1],
            fill=BLUE,
            width=3
        )

    # Latest point

    x, y = points[-1]

    canvas.create_oval(
        x - 4,
        y - 4,
        x + 4,
        y + 4,
        fill=BLUE,
        outline=""
    )

    canvas.create_text(
        25,
        12,
        text="Soil Moisture %",
        anchor="w",
        fill=MUTED,
        font=("Segoe UI", 8)
    )


# =========================================================
# RISK ENGINE
# =========================================================

def calculate_risk(moisture, rainfall, water, humidity):

    score = 0
    reasons = []

    # Dry soil
    if moisture < 30:
        score += 30
        reasons.append("low soil moisture")

    elif moisture < 45:
        score += 15
        reasons.append("moderate soil moisture")

    # Heavy rainfall
    if rainfall > 60:
        score += 25
        reasons.append("heavy rainfall")

    elif rainfall > 35:
        score += 12

    # High water level
    if water > 80:
        score += 30
        reasons.append("high water level")

    elif water > 65:
        score += 15
        reasons.append("rising water level")

    # Humidity
    if humidity > 90:
        score += 15
        reasons.append("very high humidity")

    elif humidity > 80:
        score += 8

    score = min(score, 100)

    return score, reasons


# =========================================================
# RECOMMENDATION ENGINE
# =========================================================

def generate_recommendation(
    moisture,
    rainfall,
    water,
    humidity,
    score
):

    if moisture < 30:

        return (
            "Soil moisture is low. "
            "Consider controlled irrigation and "
            "avoid unnecessary water usage."
        )

    if rainfall > 60:

        return (
            "Heavy rainfall detected. "
            "Reduce irrigation temporarily and "
            "monitor drainage and water storage."
        )

    if water > 80:

        return (
            "Water level is high. "
            "Monitor reservoir capacity and "
            "check overflow protection."
        )

    if humidity > 90:

        return (
            "Humidity is very high. "
            "Monitor crop conditions and "
            "possible fungal growth."
        )

    if score >= 30:

        return (
            "Moderate environmental risk. "
            "Continue monitoring soil moisture, "
            "rainfall and water levels."
        )

    return (
        "Environmental conditions are stable. "
        "Maintain regular monitoring and "
        "use irrigation only when required."
    )


# =========================================================
# SENSOR SIMULATION
# =========================================================

def simulate_sensor(previous, minimum, maximum, step=7):

    change = random.randint(-step, step)

    return clamp(
        previous + change,
        minimum,
        maximum
    )


# =========================================================
# UPDATE DASHBOARD
# =========================================================

def update_data():

    # Simulated sensor readings

    sensor_data["moisture"] = simulate_sensor(
        sensor_data["moisture"],
        15,
        85
    )

    sensor_data["rainfall"] = simulate_sensor(
        sensor_data["rainfall"],
        0,
        100,
        10
    )

    sensor_data["water"] = simulate_sensor(
        sensor_data["water"],
        15,
        95
    )

    sensor_data["humidity"] = simulate_sensor(
        sensor_data["humidity"],
        30,
        98
    )

    moisture = sensor_data["moisture"]
    rainfall = sensor_data["rainfall"]
    water = sensor_data["water"]
    humidity = sensor_data["humidity"]

    # Save history

    history["moisture"].append(moisture)
    history["water"].append(water)
    history["rainfall"].append(rainfall)

    for key in history:

        if len(history[key]) > MAX_HISTORY:
            history[key].pop(0)

    # Update cards

    moisture_label.config(
        text=f"{moisture}%"
    )

    rainfall_label.config(
        text=f"{rainfall} mm"
    )

    water_label.config(
        text=f"{water}%"
    )

    humidity_label.config(
        text=f"{humidity}%"
    )

    # Risk engine

    score, reasons = calculate_risk(
        moisture,
        rainfall,
        water,
        humidity
    )

    # Determine risk level

    if score >= 60:

        risk = "HIGH"
        risk_color = RED

        alert_label.config(
            text="⚠ Critical environmental conditions detected",
            fg=RED
        )

    elif score >= 30:

        risk = "MEDIUM"
        risk_color = YELLOW

        alert_label.config(
            text="⚠ Moderate environmental risk",
            fg=YELLOW
        )

    else:

        risk = "LOW"
        risk_color = GREEN

        alert_label.config(
            text="✓ No critical alerts",
            fg=GREEN
        )

    # Update risk panel

    risk_label.config(
        text=risk,
        fg=risk_color
    )

    score_label.config(
        text=f"Risk Score: {score} / 100"
    )

    progress.config(
        bg=risk_color
    )

    progress.place(
        x=0,
        y=0,
        width=int(300 * score / 100),
        height=12
    )

    if reasons:

        reason_text = "Detected: " + ", ".join(reasons)

    else:

        reason_text = "All monitored parameters are within normal range."

    risk_reason.config(
        text=reason_text
    )

    # Recommendation

    message = generate_recommendation(
        moisture,
        rainfall,
        water,
        humidity,
        score
    )

    message_label.config(
        text=message
    )

    # Graph

    draw_graph()

    # Next automatic update

    root.after(3000, update_data)


# =========================================================
# BOTTOM CONTROL BAR
# =========================================================

bottom = tk.Frame(
    root,
    bg=BG
)
bottom.pack(
    fill="x",
    padx=35,
    pady=(2, 18)
)

tk.Label(
    bottom,
    text="ESP32 Sensor Simulation  •  Risk Engine  •  Real-Time Monitoring",
    font=("Segoe UI", 8),
    bg=BG,
    fg=MUTED
).pack(side="left")

refresh = tk.Button(
    bottom,
    text="↻  Refresh Now",
    font=("Segoe UI", 9, "bold"),
    bg=BLUE,
    fg="#06111F",
    activebackground="#5BDCF7",
    activeforeground="#06111F",
    relief="flat",
    bd=0,
    padx=18,
    pady=7,
    cursor="hand2",
    command=update_data
)

refresh.pack(side="right")


# =========================================================
# START APPLICATION
# =========================================================

update_data()

root.mainloop()