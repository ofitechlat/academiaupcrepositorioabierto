import zipfile
import os
import random
import string
import math
from datetime import datetime
import json

# ---------------------------------------------------------
# IDENTIFIERS AND UTILITIES
# ---------------------------------------------------------
def generate_ode_id():
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return timestamp + random_chars

def generate_uuid():
    import uuid
    return str(uuid.uuid4())

def generate_block_id():
    now = int(datetime.now().timestamp() * 1000)
    random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=9))
    return f"block-{now}-{random_chars}"

def generate_idevice_id():
    now = int(datetime.now().timestamp() * 1000)
    random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=9))
    return f"idevice-{now}-{random_chars}"

def escape_xml(str_val):
    if not str_val: return ""
    return str_val.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&apos;")

# ---------------------------------------------------------
# PROGRAMMATIC SVG GENERATORS (PARAMETRIC GRAPHICS)
# ---------------------------------------------------------
def get_right_triangle_svg(a, b, c, opposite_lbl="a", adjacent_lbl="b", hyp_lbl="c", angle_lbl="θ"):
    """
    Generates a right triangle inline SVG styled in neon theme.
    """
    return f"""<div style="text-align:center; margin:15px 0;">
    <svg width="220" height="150" viewBox="0 0 220 150" style="display:inline-block; background:rgba(15, 23, 42, 0.4); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:10px;">
        <!-- Right angle mark -->
        <path d="M 160 110 L 160 100 L 170 100" fill="none" stroke="#6b7280" stroke-width="1.5"/>
        <!-- Triangle path -->
        <polygon points="40,110 170,110 170,30" fill="rgba(6, 182, 212, 0.12)" stroke="#06b6d4" stroke-width="2.5"/>
        <!-- Labels -->
        <!-- Adjacent side (b) -->
        <text x="105" y="130" fill="#e2e8f0" font-family="'Outfit', sans-serif" font-size="14" font-weight="600" text-anchor="middle">{adjacent_lbl} = {b}</text>
        <!-- Opposite side (a) -->
        <text x="188" y="75" fill="#e2e8f0" font-family="'Outfit', sans-serif" font-size="14" font-weight="600" text-anchor="start">{opposite_lbl} = {a}</text>
        <!-- Hypotenuse (c) -->
        <text x="90" y="60" fill="#e2e8f0" font-family="'Outfit', sans-serif" font-size="14" font-weight="600" text-anchor="middle">{hyp_lbl} = {c}</text>
        <!-- Angle theta -->
        <path d="M 60 110 A 20 20 0 0 0 57 100" fill="none" stroke="#ec4899" stroke-width="2"/>
        <text x="68" y="105" fill="#ec4899" font-family="'Outfit', sans-serif" font-size="13" font-weight="700">{angle_lbl}</text>
    </svg>
    </div>"""

def get_oblique_triangle_svg(a, b, c, A_lbl="A", B_lbl="B", C_lbl="C", a_lbl="a", b_lbl="b", c_lbl="c"):
    """
    Generates an oblique triangle inline SVG.
    """
    return f"""<div style="text-align:center; margin:15px 0;">
    <svg width="240" height="150" viewBox="0 0 240 150" style="display:inline-block; background:rgba(15, 23, 42, 0.4); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:10px;">
        <polygon points="30,120 210,120 120,30" fill="rgba(236, 72, 153, 0.08)" stroke="#ec4899" stroke-width="2.5"/>
        <!-- Side labels -->
        <text x="120" y="138" fill="#e2e8f0" font-family="'Outfit', sans-serif" font-size="14" font-weight="600" text-anchor="middle">{c_lbl} = {c}</text>
        <text x="60" y="70" fill="#e2e8f0" font-family="'Outfit', sans-serif" font-size="14" font-weight="600" text-anchor="middle">{b_lbl} = {b}</text>
        <text x="180" y="70" fill="#e2e8f0" font-family="'Outfit', sans-serif" font-size="14" font-weight="600" text-anchor="middle">{a_lbl} = {a}</text>
        <!-- Vertex angle labels -->
        <text x="20" y="115" fill="#06b6d4" font-family="'Outfit', sans-serif" font-size="13" font-weight="700">{A_lbl}</text>
        <text x="220" y="115" fill="#06b6d4" font-family="'Outfit', sans-serif" font-size="13" font-weight="700">{B_lbl}</text>
        <text x="120" y="24" fill="#06b6d4" font-family="'Outfit', sans-serif" font-size="13" font-weight="700" text-anchor="middle">{C_lbl}</text>
    </svg>
    </div>"""

def get_unit_circle_projection_svg(angle):
    """
    Generates an inline SVG showing an angle projection in the unit circle.
    """
    rad = math.radians(angle)
    cx, cy = 100, 100
    r = 75
    px = cx + r * math.cos(rad)
    py = cy - r * math.sin(rad)  # SVG y is inverted
    cos_x = cx + r * math.cos(rad)
    
    # Arc
    arc_d = ""
    if angle > 0:
        arc_r = 15
        tx = cx + arc_r * math.cos(rad)
        ty = cy - arc_r * math.sin(rad)
        large_arc = 1 if angle > 180 else 0
        arc_d = f"M {cx + arc_r} {cy} A {arc_r} {arc_r} 0 {large_arc} 0 {tx} {ty} L {cx} {cy} Z"
        
    return f"""<div style="text-align:center; margin:15px 0;">
    <svg width="200" height="200" viewBox="0 0 200 200" style="display:inline-block; background:rgba(15, 23, 42, 0.4); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:10px;">
        <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1.5"/>
        <line x1="{cx - r - 15}" y1="{cy}" x2="{cx + r + 15}" y2="{cy}" stroke="#475569" stroke-width="1"/>
        <line x1="{cx}" y1="{cy - r - 15}" x2="{cx}" y2="{cy + r + 15}" stroke="#475569" stroke-width="1"/>
        <!-- Cosine line (Blue) -->
        <line x1="{cx}" y1="{cy}" x2="{cos_x}" y2="{cy}" stroke="#3b82f6" stroke-width="3"/>
        <!-- Sine line (Pink) -->
        <line x1="{cos_x}" y1="{cy}" x2="{px}" y2="{py}" stroke="#ec4899" stroke-width="3"/>
        <!-- Radial Arm -->
        <line x1="{cx}" y1="{cy}" x2="{px}" y2="{py}" stroke="#f8fafc" stroke-width="1.5"/>
        <circle cx="{px}" cy="{py}" r="4" fill="#06b6d4"/>
        <!-- Angle Arc -->
        <path d="{arc_d}" fill="rgba(6, 182, 212, 0.25)" stroke="#06b6d4" stroke-width="1"/>
        <!-- Text Label -->
        <text x="{cx + 20}" y="{cy - 10}" fill="#06b6d4" font-family="'Outfit', sans-serif" font-size="12" font-weight="700">{angle}°</text>
    </svg>
    </div>"""

def generate_trig_circle_svg(output_path):
    """
    Generates the standalone professional trigonometric unit circle SVG file.
    """
    svg = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
    svg += '<svg width="600" height="600" viewBox="0 0 600 600" xmlns="http://www.w3.org/2000/svg">\n'
    
    # Premium background slate
    svg += '  <rect width="600" height="600" fill="#0f172a" rx="24"/>\n'
    
    # Outer border and title
    svg += '  <rect x="10" y="10" width="580" height="580" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="2" rx="16"/>\n'
    svg += '  <text x="300" y="45" fill="#f8fafc" font-family="\'Outfit\', sans-serif" font-size="20" font-weight="800" text-anchor="middle">CIRCUNFERENCIA TRIGONOMÉTRICA</text>\n'
    
    # Drawing variables
    cx, cy = 300, 320
    r = 200
    
    # Grid concentric circles
    svg += f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>\n'
    svg += f'  <circle cx="{cx}" cy="{cy}" r="{r * 0.707}" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1" stroke-dasharray="4,4"/>\n'
    svg += f'  <circle cx="{cx}" cy="{cy}" r="{r * 0.5}" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1" stroke-dasharray="4,4"/>\n'
    
    # Main Axes
    svg += f'  <line x1="{cx - r - 40}" y1="{cy}" x2="{cx + r + 40}" y2="{cy}" stroke="#64748b" stroke-width="2"/>\n'
    svg += f'  <line x1="{cx}" y1="{cy - r - 40}" x2="{cx}" y2="{cy + r + 40}" stroke="#64748b" stroke-width="2"/>\n'
    
    # Axis labels
    svg += f'  <text x="{cx + r + 50}" y="{cy + 5}" fill="#94a3b8" font-family="monospace" font-size="16" font-weight="700">X (cos)</text>\n'
    svg += f'  <text x="{cx}" y="{cy - r - 50}" fill="#94a3b8" font-family="monospace" font-size="16" font-weight="700" text-anchor="middle">Y (sen)</text>\n'
    
    # Notable angles rays, coordinates, degree and radian text
    notables = [
        {"angle": 0, "rad": "0", "cos": "1", "sin": "0", "color": "#f8fafc", "align": "start", "dx": 20, "dy": 5},
        {"angle": 30, "rad": "π/6", "cos": "√3/2", "sin": "1/2", "color": "#06b6d4", "align": "start", "dx": 15, "dy": -10},
        {"angle": 45, "rad": "π/4", "cos": "√2/2", "sin": "√2/2", "color": "#ec4899", "align": "start", "dx": 15, "dy": -15},
        {"angle": 60, "rad": "π/3", "cos": "1/2", "sin": "√3/2", "color": "#a855f7", "align": "start", "dx": 10, "dy": -20},
        {"angle": 90, "rad": "π/2", "cos": "0", "sin": "1", "color": "#f8fafc", "align": "middle", "dx": 0, "dy": -25},
        {"angle": 120, "rad": "2π/3", "cos": "-1/2", "sin": "√3/2", "color": "#a855f7", "align": "end", "dx": -10, "dy": -20},
        {"angle": 135, "rad": "3π/4", "cos": "-√2/2", "sin": "√2/2", "color": "#ec4899", "align": "end", "dx": -15, "dy": -15},
        {"angle": 150, "rad": "5π/6", "cos": "-√3/2", "sin": "1/2", "color": "#06b6d4", "align": "end", "dx": -15, "dy": -10},
        {"angle": 180, "rad": "π", "cos": "-1", "sin": "0", "color": "#f8fafc", "align": "end", "dx": -20, "dy": 5},
        {"angle": 210, "rad": "7π/6", "cos": "-√3/2", "sin": "-1/2", "color": "#06b6d4", "align": "end", "dx": -15, "dy": 20},
        {"angle": 225, "rad": "5π/4", "cos": "-√2/2", "sin": "-√2/2", "color": "#ec4899", "align": "end", "dx": -15, "dy": 25},
        {"angle": 240, "rad": "4π/3", "cos": "-1/2", "sin": "-√3/2", "color": "#a855f7", "align": "end", "dx": -10, "dy": 30},
        {"angle": 270, "rad": "3π/2", "cos": "0", "sin": "-1", "color": "#f8fafc", "align": "middle", "dx": 0, "dy": 35},
        {"angle": 300, "rad": "5π/3", "cos": "1/2", "sin": "-√3/2", "color": "#a855f7", "align": "start", "dx": 10, "dy": 30},
        {"angle": 315, "rad": "7π/4", "cos": "√2/2", "sin": "-√2/2", "color": "#ec4899", "align": "start", "dx": 15, "dy": 25},
        {"angle": 330, "rad": "11π/6", "cos": "√3/2", "sin": "-1/2", "color": "#06b6d4", "align": "start", "dx": 15, "dy": 20}
    ]
    
    for pt in notables:
        theta = math.radians(pt["angle"])
        px = cx + r * math.cos(theta)
        py = cy - r * math.sin(theta)
        
        # Ray line
        if pt["angle"] not in [0, 90, 180, 270]:
            svg += f'  <line x1="{cx}" y1="{cy}" x2="{px}" y2="{py}" stroke="{pt["color"]}" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6"/>\n'
        
        # Ray tip endpoint marker
        svg += f'  <circle cx="{px}" cy="{py}" r="4" fill="{pt["color"]}"/>\n'
        
        # Text positioning labels
        lx = px + pt["dx"]
        ly = py + pt["dy"]
        
        # Combine labels: Deg, Radian, Coordinate
        coord = f"({pt['cos']}, {pt['sin']})"
        lbl = f"{pt['angle']}° | {pt['rad']}"
        
        svg += f'  <g font-family="\'Inter\', sans-serif" font-size="11" font-weight="600" text-anchor="{pt["align"]}">\n'
        svg += f'    <text x="{lx}" y="{ly}" fill="#ffffff">{lbl}</text>\n'
        svg += f'    <text x="{lx}" y="{ly + 13}" fill="{pt["color"]}" font-size="10" font-weight="700">{coord}</text>\n'
        svg += '  </g>\n'
        
    svg += '</svg>\n'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg)

# ---------------------------------------------------------
# PARAMETRIC BANK OF PRACTICE QUESTIONS
# ---------------------------------------------------------
def generate_parametric_quizzes(module_num):
    """
    Generates a structured dynamic quiz dictionary for basic, intermediate, and advanced levels
    specifically formatted for the module_num topic.
    """
    quizzes = {"basic": [], "intermediate": [], "advanced": []}
    
    if module_num == 1:
        # Theme: Fundamentos y Ángulos
        # BASIC
        quizzes["basic"].append({
            "activityType": "selection",
            "baseText": "<p>Convierte un ángulo notable de <strong>60°</strong> a radianes exactos.</p>",
            "answers": [[True, "π/3 rad"], [False, "π/6 rad"], [False, "π/4 rad"], [False, "π/2 rad"]]
        })
        quizzes["basic"].append({
            "activityType": "selection",
            "baseText": "<p>Convierte un ángulo en radianes de <strong>3π/4 rad</strong> a grados sexagesimales.</p>",
            "answers": [[False, "120°"], [True, "135°"], [False, "150°"], [False, "145°"]]
        })
        
        # INTERMEDIATE
        quizzes["intermediate"].append({
            "activityType": "selection",
            "baseText": "<p>Halla la longitud de arco <strong>s</strong> recorrida en una circunferencia de radio <strong>r = 6 cm</strong> por un ángulo central de <strong>θ = π/3 rad</strong>.</p><p><em>Fórmula: \( s = \theta \cdot r \)</em></p>",
            "answers": [[True, "2π cm (≈ 6.28 cm)"], [False, "3π cm"], [False, "4π cm"], [False, "π cm"]]
        })
        quizzes["intermediate"].append({
            "activityType": "selection",
            "baseText": "<p>Halla el área del sector circular para una circunferencia de radio <strong>r = 4 cm</strong> y ángulo central <strong>θ = π/4 rad</strong>.</p><p><em>Fórmula: \( A = \frac{1}{2} \theta r^2 \)</em></p>",
            "answers": [[False, "4π cm²"], [True, "2π cm²"], [False, "8π cm²"], [False, "π/2 cm²"]]
        })
        
        # ADVANCED
        quizzes["advanced"].append({
            "activityType": "selection",
            "baseText": "<p>Un engranaje industrial con un radio de <strong>10 cm</strong> gira a una velocidad angular constante de <strong>3 rad/s</strong>. Calcula la velocidad lineal de un diente ubicado en el borde del engranaje.</p><p><em>Fórmula: \( v = \omega \cdot r \)</em></p>",
            "answers": [[True, "30 cm/s"], [False, "15 cm/s"], [False, "10 cm/s"], [False, "3 cm/s"]]
        })
        quizzes["advanced"].append({
            "activityType": "selection",
            "baseText": "<p>Dos ruedas dentadas están acopladas mediante una banda. La rueda A tiene un radio de <strong>rA = 12 cm</strong> y gira a una velocidad angular de <strong>ωA = 2 rad/s</strong>. Si la rueda B tiene un radio de <strong>rB = 4 cm</strong>, ¿cuál es la velocidad angular <strong>ωB</strong> de la rueda B?</p><p><em>Fórmula: \( \omega_A r_A = \omega_B r_B \)</em></p>",
            "answers": [[False, "2 rad/s"], [False, "4 rad/s"], [True, "6 rad/s"], [False, "8 rad/s"]]
        })

    elif module_num == 2:
        # Theme: Razones Trigonométricas
        # BASIC
        fig_b1 = get_right_triangle_svg(3, 4, 5, "a", "b", "c")
        quizzes["basic"].append({
            "activityType": "selection",
            "baseText": f"<p>Considera el siguiente triángulo rectángulo:</p>{fig_b1}<p>Calcula el valor exacto del <strong>coseno de θ</strong>.</p>",
            "answers": [[False, "3/5"], [True, "4/5"], [False, "3/4"], [False, "5/4"]]
        })
        quizzes["basic"].append({
            "activityType": "selection",
            "baseText": "<p>¿Cuál es la razón trigonométrica que se define como el recíproco de la secante?</p>",
            "answers": [[False, "Seno (sen)"], [True, "Coseno (cos)"], [False, "Tangente (tan)"], [False, "Cosecante (csc)"]]
        })
        
        # INTERMEDIATE
        quizzes["intermediate"].append({
            "activityType": "selection",
            "baseText": "<p>Si <strong>sen(θ) = 5/13</strong> y θ es un ángulo agudo (Cuadrante I), calcula el valor de la <strong>tangente de θ</strong>.</p>",
            "answers": [[False, "12/5"], [True, "5/12"], [False, "12/13"], [False, "5/13"]]
        })
        fig_i2 = get_right_triangle_svg("h", 12, "d", "h", "12 m", "d", "30°")
        quizzes["intermediate"].append({
            "activityType": "selection",
            "baseText": f"<p>Un árbol proyecta una sombra de <strong>12 m</strong> en el suelo cuando el ángulo de elevación del Sol es de <strong>30°</strong>:</p>{fig_i2}<p>Calcula la altura exacta <strong>h</strong> del árbol.</p>",
            "answers": [[True, "4√3 m (≈ 6.93 m)"], [False, "12√3 m"], [False, "6 m"], [False, "12 m"]]
        })
        
        # ADVANCED
        quizzes["advanced"].append({
            "activityType": "selection",
            "baseText": "<p>Desde la cima de un faro situado a <strong>80 m</strong> sobre el nivel del mar, un observador divisa dos barcos alineados en la misma dirección. Los ángulos de depresión de los barcos son de <strong>30°</strong> y <strong>45°</strong> respectivamente. Calcula la distancia exacta que separa a ambos barcos.</p>",
            "answers": [[True, "80(√3 - 1) m (≈ 58.56 m)"], [False, "80√3 m"], [False, "80 m"], [False, "40 m"]]
        })

    elif module_num == 3:
        # Theme: El Círculo Unitario
        # BASIC
        quizzes["basic"].append({
            "activityType": "selection",
            "baseText": "<p>¿En qué cuadrante el seno es estrictamente negativo y el coseno es estrictamente positivo?</p>",
            "answers": [[False, "Cuadrante II"], [False, "Cuadrante III"], [True, "Cuadrante IV"], [False, "Cuadrante I"]]
        })
        quizzes["basic"].append({
            "activityType": "selection",
            "baseText": "<p>¿Cuál es el signo algebraico de la función tangente en el <strong>Cuadrante III</strong>?</p>",
            "answers": [[True, "Positivo (+), porque sen(-) / cos(-) = +"], [False, "Negativo (-)"], [False, "Cero (0)"]]
        })
        
        # INTERMEDIATE
        fig_i1 = get_unit_circle_projection_svg(120)
        quizzes["intermediate"].append({
            "activityType": "selection",
            "baseText": f"<p>Para el ángulo notable de <strong>120°</strong> proyectado en el círculo unitario:</p>{fig_i1}<p>Calcula el valor exacto de <strong>cos(120°)</strong>.</p>",
            "answers": [[False, "1/2"], [True, "-1/2"], [False, "-√3/2"], [False, "√3/2"]]
        })
        fig_i2 = get_unit_circle_projection_svg(315)
        quizzes["intermediate"].append({
            "activityType": "selection",
            "baseText": f"<p>Para el ángulo notable de <strong>315° (7π/4 rad)</strong>:</p>{fig_i2}<p>Calcula el valor exacto de <strong>sen(315°)</strong>.</p>",
            "answers": [[False, "√2/2"], [True, "-√2/2"], [False, "-1/2"], [False, "-√3/2"]]
        })
        
        # ADVANCED
        quizzes["advanced"].append({
            "activityType": "selection",
            "baseText": "<p>Halla el valor exacto del ángulo negativo evaluado en el círculo unitario: <strong>tan(-240°)</strong>.</p>",
            "answers": [[True, "-√3"], [False, "√3"], [False, "-√3/3"], [False, "√3/3"]]
        })
        quizzes["advanced"].append({
            "activityType": "selection",
            "baseText": "<p>Si el punto terminal de un ángulo θ en el círculo unitario está ubicado en las coordenadas \( \\left( -\\frac{\\sqrt{5}}{3}, -\\frac{2}{3} \\right) \), calcula el valor exacto de la <strong>cotangente (cot θ)</strong>.</p>",
            "answers": [[True, "√5/2"], [False, "-√5/2"], [False, "2/√5"], [False, "-2/√5"]]
        })

    elif module_num == 4:
        # Theme: Identidades y Ecuaciones
        # BASIC
        quizzes["basic"].append({
            "activityType": "selection",
            "baseText": "<p>Simplifica al máximo la expresión trigonométrica: <strong>sen(θ) · csc(θ)</strong>.</p>",
            "answers": [[True, "1"], [False, "0"], [False, "tan(θ)"], [False, "cos(θ)"]]
        })
        quizzes["basic"].append({
            "activityType": "selection",
            "baseText": "<p>Por la identidad pitagórica fundamental, ¿a qué equivale la expresión <strong>1 - sen²(θ)</strong>?</p>",
            "answers": [[False, "sen²(θ)"], [True, "cos²(θ)"], [False, "tan²(θ)"], [False, "1"]]
        })
        
        # INTERMEDIATE
        quizzes["intermediate"].append({
            "activityType": "selection",
            "baseText": "<p>Resuelve la ecuación trigonométrica <strong>sen(x) = √3/2</strong> para el intervalo <strong>x ∈ [0, 2π]</strong>.</p>",
            "answers": [[True, "[π/3, 2π/3] (60° y 120°)"], [False, "[π/6, 5\u03c0/6]"], [False, "[\u03c0/3, 4\u03c0/3]"], [False, "[2\u03c0/3, 4\u03c0/3]"]]
        })
        quizzes["intermediate"].append({
            "activityType": "selection",
            "baseText": "<p>Resuelve la ecuación trigonométrica lineal <strong>2·cos(x) + 1 = 0</strong> para <strong>x ∈ [0, 2π]</strong>.</p>",
            "answers": [[False, "[\u03c0/3, 5\u03c0/3]"], [True, "[2π/3, 4π/3] (120° y 240°)"], [False, "[2\u03c0/3, 5\u03c0/3]"], [False, "[\u03c0/6, 11\u03c0/6]"]]
        })
        
        # ADVANCED
        quizzes["advanced"].append({
            "activityType": "selection",
            "baseText": "<p>Resuelve la ecuación cuadrática <strong>2·cos²(x) - cos(x) - 1 = 0</strong> en el intervalo cerrado <strong>x ∈ [0, 2π]</strong>.</p>",
            "answers": [[True, "[0, 2π/3, 4π/3, 2π]"], [False, "[0, \u03c0/3, 5\u03c0/3]"], [False, "[\u03c0/2, 2\u03c0/3, 4\u03c0/3]"], [False, "[0, 2\u03c0/3, 4\u03c0/3]"]]
        })
        quizzes["advanced"].append({
            "activityType": "selection",
            "baseText": "<p>Simplifica completamente la expresión racional trigonométrica: <br> \( \\frac{1}{1 - sen(x)} + \\frac{1}{1 + sen(x)} \)</p>",
            "answers": [[True, "2·sec²(x)"], [False, "2·csc²(x)"], [False, "2·cos²(x)"], [False, "2"]]
        })

    elif module_num == 5:
        # Theme: Triángulos Oblicuángulos
        # BASIC
        fig_b1 = get_oblique_triangle_svg("A", "B", "C", "A", "B", "C", "a", "b", "c")
        quizzes["basic"].append({
            "activityType": "selection",
            "baseText": f"<p>En un triángulo oblicuángulo como el de la figura:</p>{fig_b1}<p>Si el lado <strong>a = 10</strong>, <strong>sen(A) = 0.5</strong> y <strong>sen(B) = 0.8</strong>, calcula la longitud del lado <strong>b</strong> usando la Ley de Senos.</p>",
            "answers": [[True, "16"], [False, "12"], [False, "10"], [False, "8"]]
        })
        quizzes["basic"].append({
            "activityType": "selection",
            "baseText": "<p>¿Qué ley matemática es la más directa para calcular los ángulos de un triángulo oblicuángulo cuando se conocen exclusivamente las longitudes de sus tres lados?</p>",
            "answers": [[False, "Ley de Senos"], [True, "Ley de Cosenos"], [False, "Teorema de Pitágoras"], [False, "Ley de Tangentes"]]
        })
        
        # INTERMEDIATE
        fig_i1 = get_oblique_triangle_svg("a", 5, 8, "A", "B", "60°", "a", "b", "c")
        quizzes["intermediate"].append({
            "activityType": "selection",
            "baseText": f"<p>Resuelve el lado faltante <strong>c</strong> de un triángulo con lados <strong>a = 5</strong>, <strong>b = 8</strong> y el ángulo comprendido de <strong>C = 60°</strong>:</p>{fig_i1}<p>Aplica la Ley de Cosenos.</p>",
            "answers": [[True, "7"], [False, "9"], [False, "√89"], [False, "5.5"]]
        })
        quizzes["intermediate"].append({
            "activityType": "selection",
            "baseText": "<p>Resuelve el caso ambiguo (LLA). En un triángulo con lado <strong>a = 12</strong>, lado <strong>b = 10</strong> y el ángulo opuesto <strong>A = 45°</strong>. Calcula el valor exacto de <strong>sen(B)</strong>.</p>",
            "answers": [[True, "5√2/12 (≈ 0.589)"], [False, "√2/2"], [False, "0.5"], [False, "0.75"]]
        })
        
        # ADVANCED
        quizzes["advanced"].append({
            "activityType": "selection",
            "baseText": "<p>Dos embarcaciones parten simultáneamente de un mismo puerto en trayectorias rectilíneas que forman un ángulo de <strong>120°</strong>. El barco A navega a una velocidad de <strong>20 nudos</strong>, y el barco B navega a <strong>15 nudos</strong>. ¿Qué distancia exacta separa a los dos barcos al cabo de 2 horas?</p>",
            "answers": [[True, "60.8 millas (2√725 millas)"], [False, "70 millas"], [False, "50 millas"], [False, "65 millas"]]
        })
        quizzes["advanced"].append({
            "activityType": "selection",
            "baseText": "<p>Para medir la altura <strong>h</strong> de una montaña inaccesible, un topógrafo toma dos lecturas de ángulos de elevación desde el suelo en línea recta hacia la montaña, separadas entre sí por una distancia de <strong>100 m</strong>. Las lecturas de los ángulos de elevación son de <strong>30°</strong> y <strong>45°</strong> respectivamente. Calcula la altura aproximada de la montaña.</p>",
            "answers": [[True, "136.6 m (50(√3 + 1) m)"], [False, "100 m"], [False, "50√3 m"], [False, "100(√3 - 1) m"]]
        })
        
    return quizzes

# ---------------------------------------------------------
# STRUCTURED UNIVERSITY LEVEL COURSE DATA
# ---------------------------------------------------------
def create_course_content():
    return [
        {
            "title": "Inicio",
            "content": """<h1>Trigonometría para Nivelación Universitaria</h1>
            <p>Bienvenido al curso de <strong>Trigonometría para Nivelación Universitaria</strong>. Este espacio ha sido especialmente estructurado para dotar a los estudiantes de primer ingreso universitario de los cimientos conceptuales, analíticos e interactivos requeridos en las cátedras de cálculo, física e ingeniería.</p>
            <div style="background: #ecfeff; border: 1px solid #cffafe; border-left: 4px solid #06b6d4; padding: 15px; border-radius: 8px; margin: 20px 0;">
                <p style="margin: 0; color: #0f172a;"><strong>Objetivo del Curso:</strong> Dominar la relación entre las razones geométricas de los triángulos y la funciones circulares en el plano analítico, aplicando identidades, ecuaciones y leyes de resolución en escenarios teóricos e interactivos en 3 niveles de dificultad progresivos.</p>
            </div>
            <h3>Estructura del Curso:</h3>
            <ul>
                <li><strong>Módulo 1: Fundamentos y Ángulos</strong> (Medición sexagesimal y cíclica).</li>
                <li><strong>Módulo 2: Razones Trigonométricas</strong> (Triángulos rectángulos y aplicaciones).</li>
                <li><strong>Módulo 3: El Círculo Unitario</strong> (Funciones en el plano analítico y coordenadas).</li>
                <li><strong>Módulo 4: Identidades y Ecuaciones</strong> (Simplificaciones y raíces).</li>
                <li><strong>Módulo 5: Triángulos Oblicuángulos</strong> (Leyes de Senos y Cosenos).</li>
            </ul>""",
            "quiz": None,
            "children": [
                {
                    "title": "Módulo 1: Fundamentos y Ángulos",
                    "content": """<h2>Sistemas de Medición Angular</h2>
                    <p>En el plano matemático, un ángulo se genera mediante la rotación de un rayo alrededor de un punto fijo denominado vértice. Para su análisis cuantitativo, empleamos fundamentalmente dos sistemas:</p>
                    <ol>
                        <li><strong>Grados sexagesimales (°)</strong>: Define una revolución completa como 360°. Es el sistema heredado históricamente y muy común en geometría plana básica.</li>
                        <li><strong>Radianes (rad)</strong>: Define una revolución completa en términos de la longitud del arco del círculo unitario, donde una vuelta completa equivale a \( 2\pi \) radianes. Un radián es la medida del ángulo central que subtiende un arco de longitud igual al radio.</li>
                    </ol>
                    <h3>Equivalencia Fundamental:</h3>
                    <div class="formula-box" style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid #db2777; padding:12px 18px; border-radius:8px; font-family:monospace; color:#0f172a; font-weight:600; margin:15px 0;">
                        180° = π rad &nbsp;&nbsp;⇒&nbsp;&nbsp; Radianes = Grados × (π / 180)<br>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒&nbsp;&nbsp; Grados = Radianes × (180 / π)
                    </div>
                    <h3>Longitud de Arco y Velocidad Angular</h3>
                    <p>En una circunferencia de radio \( r \), la longitud de arco \( s \) correspondiente a un ángulo central \( \theta \) en radianes es:</p>
                    <p align="center">\( s = \theta \cdot r \)</p>
                    <p>Asimismo, en el movimiento circular, la velocidad lineal \( v \) se vincula con la velocidad angular \( \omega \) en radianes por segundo a través de: \( v = \omega \cdot r \).</p>""",
                    "quiz": generate_parametric_quizzes(1),
                    "children": []
                },
                {
                    "title": "Módulo 2: Razones Trigonométricas",
                    "content": """<h2>Triángulos Rectángulos</h2>
                    <p>Para un ángulo agudo \( \theta \) ubicado dentro de un triángulo rectángulo, definimos las seis razones trigonométricas clásicas basándonos en las longitudes de los catetos opuesto (CO), adyacente (CA) y la hipotenusa (H).</p>
                    <table border="1" cellpadding="8" style="border-collapse:collapse; border-color:#cbd5e1; width:100%; text-align:center; background:#ffffff; margin:15px 0;">
                        <tr style="background:#f1f5f9; color:#0f172a; font-weight:700;">
                            <th>Razón Trigonométrica</th>
                            <th>Abreviatura</th>
                            <th>Fórmula del Triángulo</th>
                        </tr>
                        <tr>
                            <td><strong>Seno</strong></td>
                            <td>sen(θ)</td>
                            <td>Opuesto / Hipotenusa (CO / H)</td>
                        </tr>
                        <tr>
                            <td><strong>Coseno</strong></td>
                            <td>cos(θ)</td>
                            <td>Adyacente / Hipotenusa (CA / H)</td>
                        </tr>
                        <tr>
                            <td><strong>Tangente</strong></td>
                            <td>tan(θ)</td>
                            <td>Opuesto / Adyacente (CO / CA)</td>
                        </tr>
                        <tr>
                            <td><strong>Cosecante</strong></td>
                            <td>csc(θ)</td>
                            <td>Hipotenusa / Opuesto (H / CO)</td>
                        </tr>
                        <tr>
                            <td><strong>Secante</strong></td>
                            <td>sec(θ)</td>
                            <td>Hipotenusa / Adyacente (H / CA)</td>
                        </tr>
                        <tr>
                            <td><strong>Cotangente</strong></td>
                            <td>cot(θ)</td>
                            <td>Adyacente / Opuesto (CA / CO)</td>
                        </tr>
                    </table>
                    <h3>Identidades Recíprocas:</h3>
                    <p align="center">
                        \( csc(\theta) = \\frac{1}{sen(\theta)} \) &nbsp;&nbsp;|&nbsp;&nbsp;
                        \( sec(\theta) = \\frac{1}{cos(\theta)} \) &nbsp;&nbsp;|&nbsp;&nbsp;
                        \( cot(\theta) = \\frac{1}{tan(\theta)} \)
                    </p>""",
                    "quiz": generate_parametric_quizzes(2),
                    "children": []
                },
                {
                    "title": "Módulo 3: El Círculo Unitario",
                    "content": """<h2>El Círculo Unitario Trigonométrico</h2>
                    <p>El Círculo Unitario es una herramienta analítica sumamente potente. Se define como una circunferencia centrada en el origen \( (0,0) \) con un radio exactamente igual a <strong>1</strong>. Su ecuación matemática es:</p>
                    <p align="center"><strong>\( x^2 + y^2 = 1 \)</strong></p>
                    <p>Si trazamos un ángulo \( \theta \) en posición estándar (medido desde el eje X positivo contrarreloj), la intersección del lado terminal con el círculo define un punto \( P(x, y) \). De este modo, generalizamos las funciones trigonométricas para cualquier ángulo:</p>
                    <div class="formula-box" style="background:#f8fafc; border:1px solid #e2e8f0; border-left:4px solid #a855f7; padding:12px 18px; border-radius:8px; font-family:monospace; color:#0f172a; font-weight:600; margin:15px 0;">
                        cos(θ) = x<br>
                        sen(θ) = y<br>
                        tan(θ) = y / x &nbsp;(para x &ne; 0)
                    </div>
                    <h3>Visualización Profesional de la Circunferencia</h3>
                    <p>A continuación se presenta la circunferencia trigonométrica vectorial detallando los ángulos notables más utilizados, expresados simultáneamente en grados, radianes y sus coordenadas cartesianas exactas:</p>
                    <div style="text-align:center; margin:20px 0;">
                        <img src="resources/trig_circle.svg" alt="Circunferencia Trigonométrica Profesional" style="max-width:100%; width:450px; border-radius:16px; box-shadow:0 10px 25px rgba(0,0,0,0.05); border:1px solid #e2e8f0;"/>
                    </div>
                    <h3>Signos de las Funciones por Cuadrantes:</h3>
                    <ul>
                        <li><strong>Cuadrante I</strong> (0° a 90°): Todas las funciones son positivas (+).</li>
                        <li><strong>Cuadrante II</strong> (90° a 180°): Solo Seno y Cosecante son positivas (+).</li>
                        <li><strong>Cuadrante III</strong> (180° a 270°): Solo Tangente y Cotangente son positivas (+).</li>
                        <li><strong>Cuadrante IV</strong> (270° a 360°): Solo Coseno y Secante son positivas (+).</li>
                    </ul>""",
                    "quiz": generate_parametric_quizzes(3),
                    "children": []
                },
                {
                    "title": "Módulo 4: Identidades y Ecuaciones",
                    "content": """<h2>Identidades Trigonométricas Fundamentales</h2>
                    <p>Una identidad trigonométrica es una igualdad que vincula funciones trigonométricas y se cumple para todos los valores del ángulo en los que las funciones están definidas.</p>
                    <h3>Identidades Pitagóricas:</h3>
                    <p align="center">
                        <strong>\( sen^2(\theta) + cos^2(\theta) = 1 \)</strong><br>
                        \( 1 + tan^2(\theta) = sec^2(\theta) \)<br>
                        \( 1 + cot^2(\theta) = csc^2(\theta) \)
                    </p>
                    <h3>Identidades del Ángulo Doble:</h3>
                    <p align="center">
                        \( sen(2\theta) = 2 \cdot sen(\theta)cos(\theta) \)<br>
                        \( cos(2\theta) = cos^2(\theta) - sen^2(\theta) \)
                    </p>
                    <h2>Ecuaciones Trigonométricas</h2>
                    <p>A diferencia de las identidades, las ecuaciones trigonométricas se cumplen únicamente para ciertos valores específicos del ángulo. Al resolver una ecuación trigonométrica, es crucial especificar el dominio (por ejemplo, \( [0, 2\pi] \)) y tomar en consideración que las funciones son periódicas, pudiendo existir múltiples soluciones en una revolución.</p>""",
                    "quiz": generate_parametric_quizzes(4),
                    "children": []
                },
                {
                    "title": "Módulo 5: Triángulos Oblicuángulos",
                    "content": """<h2>Leyes de Senos y Cosenos</h2>
                    <p>Los triángulos oblicuángulos son aquellos que no poseen ningún ángulo de 90° (ángulo recto). Para resolverlos (encontrar la longitud de sus tres lados y la medida de sus tres ángulos) aplicamos dos teoremas fundamentales:</p>
                    
                    <h3>1. Ley de Senos</h3>
                    <p>Establece que las longitudes de los lados de un triángulo son proporcionales a los senos de sus respectivos ángulos opuestos:</p>
                    <p align="center" style="font-size:1.15rem; color:#0891b2;">
                        <strong>\( \\frac{a}{sen(A)} = \\frac{b}{sen(B)} = \\frac{c}{sen(C)} \)</strong>
                    </p>
                    <p><em>Aplicación ideal:</em> Cuando conocemos un lado y dos ángulos (ALA, LAA), o cuando conocemos dos lados y el ángulo opuesto a uno de ellos (LLA - caso ambiguo).</p>
                    
                    <h3>2. Ley de Cosenos</h3>
                    <p>Es una generalización del Teorema de Pitágoras aplicable a cualquier triángulo. Relaciona un lado con los otros dos y el coseno del ángulo comprendido entre ellos:</p>
                    <p align="center" style="font-size:1.15rem; color:#db2777;">
                        <strong>\( c^2 = a^2 + b^2 - 2ab \cdot cos(C) \)</strong>
                    </p>
                    <p>U análogamente para los otros lados:<br>
                       \( a^2 = b^2 + c^2 - 2bc \cdot cos(A) \)<br>
                       \( b^2 = a^2 + c^2 - 2ac \cdot cos(B) \)</p>
                    <p><em>Aplicación ideal:</em> Cuando conocemos dos lados y el ángulo comprendido entre ellos (LAL), o cuando conocemos los tres lados del triángulo (LLL).</p>""",
                    "quiz": generate_parametric_quizzes(5),
                    "children": []
                }
            ]
        }
    ]

# ---------------------------------------------------------
# XML COURSE SERIALIZER (COMPATIBLE WITH eXeLearning v4)
# ---------------------------------------------------------
def generate_content_xml(meta, course_data):
    ode_id = generate_ode_id()
    version_id = generate_ode_id()
    
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<!DOCTYPE ode SYSTEM "content.dtd">\n'
    xml += '<ode xmlns="http://www.intef.es/xsd/ode" version="2.0">\n'
    
    # userPreferences, resources, and properties
    xml += '<userPreferences>\n  <userPreference>\n    <key>theme</key>\n    <value>base</value>\n  </userPreference>\n</userPreferences>\n'
    xml += '<odeResources>\n'
    xml += f'  <odeResource><key>odeId</key><value>{ode_id}</value></odeResource>\n'
    xml += f'  <odeResource><key>odeVersionId</key><value>{version_id}</value></odeResource>\n'
    xml += f'  <odeResource><key>exe_version</key><value>4.0.0</value></odeResource>\n'
    xml += '</odeResources>\n'
    xml += '<odeProperties>\n'
    xml += f'  <odeProperty><key>pp_title</key><value>{escape_xml(meta["title"])}</value></odeProperty>\n'
    xml += '  <odeProperty><key>pp_lang</key><value>es</value></odeProperty>\n'
    xml += '  <odeProperty><key>pp_theme</key><value>base</value></odeProperty>\n'
    xml += '  <odeProperty><key>pp_exelearning_version</key><value>v4.0.0</value></odeProperty>\n'
    xml += f'  <odeProperty><key>pp_modified</key><value>{int(datetime.now().timestamp() * 1000)}</value></odeProperty>\n'
    xml += '</odeProperties>\n'
    
    xml += '<odeNavStructures>\n'
    
    # Flatten course tree structure
    pages = []
    def flatten_data(node, parent_id=None):
        page_id = generate_uuid()
        pages.append({
            "id": page_id,
            "parentId": parent_id,
            "title": node["title"],
            "content": node["content"],
            "quiz": node.get("quiz")
        })
        for child in node.get("children", []):
            flatten_data(child, page_id)
            
    for root_node in course_data:
        flatten_data(root_node)
        
    # Serialize navigation and components
    for i, page in enumerate(pages):
        xml += '  <odeNavStructure>\n'
        xml += f'    <odePageId>{page["id"]}</odePageId>\n'
        xml += f'    <odeParentPageId>{page["parentId"] or ""}</odeParentPageId>\n'
        xml += f'    <pageName>{escape_xml(page["title"])}</pageName>\n'
        xml += f'    <odeNavStructureOrder>{i}</odeNavStructureOrder>\n'
        xml += '    <odeNavStructureProperties><odeNavStructureProperty><key>titlePage</key><value>'+escape_xml(page["title"])+'</value></odeNavStructureProperty></odeNavStructureProperties>\n'
        
        xml += '    <odePagStructures>\n'
        
        # --- COMPONENT 1: THEORY TEXT ---
        # Add dynamic authorship headers/footers to fulfill Ofitech.lat and Academia UPC open repository credits
        header_banner = (
            "<div style=\"margin-bottom: 20px; font-size: 0.85rem; color: #94a3b8; font-family: sans-serif; line-height: 1.6;\">"
            "🎓 <strong>Recurso Educativo Abierto para Docentes</strong> • Creado por <a href=\"https://ofitech.lat/clases\" target=\"_blank\" style=\"color: #06b6d4; text-decoration: none; font-weight: 600;\">Ofitech.lat</a> para el Repositorio Abierto de Academia UPC • Licencia: <strong>Fair Use (Uso Justo)</strong>"
            "</div>"
        )
        
        footer_block = (
            "<hr style=\"border: 0; border-top: 1px solid rgba(255,255,255,0.06); margin: 30px 0 15px 0;\"/>"
            "<div style=\"font-size: 0.85rem; color: #94a3b8; text-align: center; font-family: sans-serif; line-height: 1.6;\">"
            "<p style=\"margin-bottom: 6px;\">"
            "🎓 <strong>Recursos Abiertos para Docentes</strong> desarrollados por <a href=\"https://ofitech.lat/clases\" target=\"_blank\" style=\"color: #06b6d4; text-decoration: none; font-weight: 600;\">Ofitech.lat</a> para el Repositorio Abierto de Academia UPC."
            "</p>"
            "<p style=\"margin-bottom: 6px;\">"
            "Uso regulado bajo los términos de la licencia de <strong>Fair Use (Uso Justo)</strong>. Código fuente y recursos en <a href=\"https://github.com/ofitechlat/academiaupcrepositorioabierto.git\" target=\"_blank\" style=\"color: #ec4899; text-decoration: none; font-weight: 600;\">GitHub</a>."
            "</p>"
            "</div>"
        )
        
        full_theory_html = header_banner + page["content"] + footer_block
        b_id_theory = generate_block_id()
        xml += f'      <odePagStructure><odePageId>{page["id"]}</odePageId><odeBlockId>{b_id_theory}</odeBlockId><blockName>Teoría del Tema</blockName><odePagStructureOrder>0</odePagStructureOrder><odePagStructureProperties/><odeComponents>\n'
        xml += f'        <odeComponent><odePageId>{page["id"]}</odePageId><odeBlockId>{b_id_theory}</odeBlockId><odeIdeviceId>{generate_idevice_id()}</odeIdeviceId><odeIdeviceTypeName>FreeTextIdevice</odeIdeviceTypeName><htmlView><![CDATA[{full_theory_html}]]></htmlView><jsonProperties>{{}}</jsonProperties><odeComponentsOrder>0</odeComponentsOrder></odeComponent>\n'
        xml += '      </odeComponents></odePagStructure>\n'
        
        # If this is not the Welcome/Home node, inject Interactive Solver & practices!
        if page["quiz"]:
            # --- COMPONENT 2: INTERACTIVE SOLVER IFRAME ---
            b_id_solver = generate_block_id()
            iframe_html = '<h2 style="margin-top:20px;">Simulador Interactivo Práctico</h2><p>Interactúa con el siguiente simulador para resolver de manera gráfica e instantánea cualquier problema relacionado con el tema actual:</p><iframe src="resources/trig_solver.html" style="width:100%; height:750px; border:none; border-radius:16px; box-shadow:0 10px 25px rgba(0,0,0,0.05); border:1px solid #cbd5e1; background:#f8fafc;"></iframe>'
            xml += f'      <odePagStructure><odePageId>{page["id"]}</odePageId><odeBlockId>{b_id_solver}</odeBlockId><blockName>Simulador Interactivo</blockName><odePagStructureOrder>1</odePagStructureOrder><odePagStructureProperties/><odeComponents>\n'
            xml += f'        <odeComponent><odePageId>{page["id"]}</odePageId><odeBlockId>{b_id_solver}</odeBlockId><odeIdeviceId>{generate_idevice_id()}</odeIdeviceId><odeIdeviceTypeName>FreeTextIdevice</odeIdeviceTypeName><htmlView><![CDATA[{iframe_html}]]></htmlView><jsonProperties>{{}}</jsonProperties><odeComponentsOrder>0</odeComponentsOrder></odeComponent>\n'
            xml += '      </odeComponents></odePagStructure>\n'
            
            # --- COMPONENT 3, 4, 5: EVALUATION PRACTICES BY DIFFICULTY ---
            difficulty_labels = [("basic", "Práctica - Nivel Básico", 2), 
                                 ("intermediate", "Práctica - Nivel Intermedio", 3), 
                                 ("advanced", "Práctica - Nivel Avanzado", 4)]
            
            for diff_key, diff_title, order_idx in difficulty_labels:
                q_b_id = generate_block_id()
                xml += f'      <odePagStructure><odePageId>{page["id"]}</odePageId><odeBlockId>{q_b_id}</odeBlockId><blockName>{diff_title}</blockName><odePagStructureOrder>{order_idx}</odePagStructureOrder><odePagStructureProperties/><odeComponents>\n'
                
                # Setup JSON for eXeLearning Form Idevice
                questions_data = []
                for q in page["quiz"][diff_key]:
                    q_id = generate_uuid()
                    q_obj = {
                        "id": q_id,
                        "activityType": "selection",
                        "baseText": q["baseText"],
                        "feedbackRight": "<p><strong>¡Correcto!</strong> Fantástico análisis matemático.</p>",
                        "feedbackWrong": "<p><strong>Incorrecto.</strong> Te sugerimos interactuar con el Simulador de arriba para visualizar las proyecciones o repasar los conceptos fundamentales del módulo.</p>",
                        "suggestion": "",
                        "order": 0,
                        "selectionType": "single",
                        "answers": q["answers"]
                    }
                    questions_data.append(q_obj)
                
                json_props = {
                    "ideviceId": "formIdevice",
                    "eXeFormInstructions": f"<p>Resuelve las siguientes preguntas de <strong>{diff_title}</strong> para consolidar y evaluar tu aprendizaje.</p>",
                    "questionsData": questions_data,
                    "dropdownPassRate": "5",
                    "addBtnAnswers": True,
                    "showSlider": False
                }
                
                xml += f'        <odeComponent><odePageId>{page["id"]}</odePageId><odeBlockId>{q_b_id}</odeBlockId><odeIdeviceId>{generate_idevice_id()}</odeIdeviceId><odeIdeviceTypeName>form</odeIdeviceTypeName><htmlView><![CDATA[]]></htmlView><jsonProperties><![CDATA[{json.dumps(json_props)}]]></jsonProperties><odeComponentsOrder>0</odeComponentsOrder></odeComponent>\n'
                xml += '      </odeComponents></odePagStructure>\n'
                
        xml += '    </odePagStructures>\n'
        xml += '  </odeNavStructure>\n'
        
    xml += '</odeNavStructures>\n'
    xml += '</ode>'
    return xml

# ---------------------------------------------------------
# MAIN PACKAGING ENGINE
# ---------------------------------------------------------
def main():
    meta = {"title": "Curso Universitario de Trigonometría Interactiva"}
    print("Iniciando generación del contenido paramétrico del curso...")
    course_data = create_course_content()
    
    print("Generando XML del contenido de eXeLearning compatible con v4...")
    content_xml = generate_content_xml(meta, course_data)
    
    with open("content.xml", "w", encoding="utf-8") as f:
        f.write(content_xml)
        
    # Generate standalone trigonometric circle SVG
    print("Generando circunferencia trigonométrica vectorial (trig_circle.svg)...")
    generate_trig_circle_svg("trig_circle.svg")
    
    # Save DTD for eXeLearning compatibility
    dtd_content = """<!ELEMENT ode (userPreferences?, odeResources?, odeProperties?, odeNavStructures)>
<!ATTLIST ode xmlns CDATA #FIXED "http://www.intef.es/xsd/ode" version CDATA #IMPLIED>
<!ELEMENT userPreferences (userPreference*)><ELEMENT userPreference (key, value)>
<!ELEMENT odeResources (odeResource*)><ELEMENT odeResource (key, value)>
<!ELEMENT odeProperties (odeProperty*)><ELEMENT odeProperty (key, value)>
<!ELEMENT key (#PCDATA)><ELEMENT value (#PCDATA)>
<!ELEMENT odeNavStructures (odeNavStructure*)><ELEMENT odeNavStructure (odePageId, odeParentPageId, pageName, odeNavStructureOrder, odeNavStructureProperties?, odePagStructures?)>
<!ELEMENT odePageId (#PCDATA)><ELEMENT odeParentPageId (#PCDATA)><ELEMENT pageName (#PCDATA)><ELEMENT odeNavStructureOrder (#PCDATA)>
<!ELEMENT odeNavStructureProperties (odeNavStructureProperty*)><ELEMENT odeNavStructureProperty (key, value)>
<!ELEMENT odePagStructures (odePagStructure*)><ELEMENT odePagStructure (odePageId, odeBlockId, blockName, iconName?, odePagStructureOrder, odePagStructureProperties?, odeComponents?)>
<!ELEMENT odeBlockId (#PCDATA)><ELEMENT blockName (#PCDATA)><ELEMENT iconName (#PCDATA)><ELEMENT odePagStructureOrder (#PCDATA)>
<!ELEMENT odePagStructureProperties (odePagStructureProperty*)><ELEMENT odePagStructureProperty (key, value)>
<!ELEMENT odeComponents (odeComponent*)><ELEMENT odeComponent (odePageId, odeBlockId, odeIdeviceId, odeIdeviceTypeName, htmlView?, jsonProperties?, odeComponentsOrder, odeComponentsProperties?)>
<!ELEMENT odeIdeviceId (#PCDATA)><ELEMENT odeIdeviceTypeName (#PCDATA)><ELEMENT htmlView (#PCDATA)><ELEMENT jsonProperties (#PCDATA)><ELEMENT odeComponentsOrder (#PCDATA)>
<!ELEMENT odeComponentsProperties (odeComponentsProperty*)><ELEMENT odeComponentsProperty (key, value)>"""
    with open("content.dtd", "w", encoding="utf-8") as f:
        f.write(dtd_content)

    # Packaging ZIP .elpx structure
    print("Empaquetando en archivo nativo trigonometricas.elpx...")
    if os.path.exists("plantilla.elpx"):
        with zipfile.ZipFile("plantilla.elpx", 'r') as template_zip:
            with zipfile.ZipFile("trigonometricas.elpx", 'w', zipfile.ZIP_DEFLATED) as new_zip:
                # Copy original files except content xml/dtd
                for item in template_zip.infolist():
                    if item.filename not in ["content.xml", "content.dtd"] and not item.filename.startswith("content/resources/"):
                        new_zip.writestr(item, template_zip.read(item.filename))
                
                # Write generated content xml and dtd
                new_zip.writestr("content.xml", content_xml)
                new_zip.writestr("content.dtd", dtd_content)
                
                # Inject resources inside content/resources/
                new_zip.write("trig_circle.svg", "content/resources/trig_circle.svg")
                new_zip.write("trig_solver.html", "content/resources/trig_solver.html")
        print("¡Proceso finalizado! Archivo 'trigonometricas.elpx' generado con éxito con todos los recursos locales y simuladores.")
    else:
        # Fallback to plain zip if plantilla is not present
        with zipfile.ZipFile("trigonometricas.elpx", 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write("content.xml")
            zipf.write("content.dtd")
            zipf.write("trig_circle.svg", "content/resources/trig_circle.svg")
            zipf.write("trig_solver.html", "content/resources/trig_solver.html")
        print("Advertencia: 'plantilla.elpx' no encontrado. Generando ZIP plano con recursos. Se recomienda disponer de la plantilla para asegurar el diseño nativo de eXeLearning.")

if __name__ == "__main__":
    main()
