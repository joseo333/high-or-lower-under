import streamlit as st
import random
import streamlit.components.v1 as components

# Artist data with name, monthly listeners, and photo path
ARTISTS = {
    "cluster": {"listeners": 477479, "photo": "cluster.jpg"},
    "cero": {"listeners": 44548, "photo": "cero.jpg"},
    "sixup": {"listeners": 31822, "photo": "sixup.jpg"},
    "enzocerobulto": {"listeners": 45134, "photo": "enzocerobulto.jpg"},
    "shako": {"listeners": 32544, "photo": "shako.jpg"},
    "frozouda": {"listeners": 127944, "photo": "frozouda.jpg"},
    "matiasenchufe": {"listeners": 13974, "photo": "matiasenchufe.jpg"},
    "magnesio": {"listeners": 31947, "photo": "magnesio.jpg"},
    "bebox": {"listeners": 2600, "photo": "bebox.jpg"},
    "blagh": {"listeners": 40656, "photo": "blagh.jpg"},
    "2uu!": {"listeners": 22279, "photo": "2uu.jpg"},
    "huntr": {"listeners": 22172, "photo": "huntr.jpg"},
    "eleiki": {"listeners": 653, "photo": "eleiki.jpg"},
    "hepa": {"listeners": 20052, "photo": "hepa.jpg"},
    "agusdelusion": {"listeners": 1538, "photo": "agusdelusion.jpg"},
    "nachotheplug": {"listeners": 16454, "photo": "nachotheplug.jpg"},
    "juicynise": {"listeners": 70000, "photo": "juicynise.jpg"},
    "doly flackko": {"listeners": 180000, "photo": "dolyflackko.jpg"},
    "perswave": {"listeners": 23688, "photo": "perswave.jpg"},
    "bic": {"listeners": 18000, "photo": "bic.jpg"},
    "ventrip": {"listeners": 8716, "photo": "ventrip.jpg"},
    "isma": {"listeners": 19341, "photo": "isma.jpg"},
    "choosey": {"listeners": 3868, "photo": "choosey.jpg"},
    "tobias lil polenta": {"listeners": 811, "photo": "tobias.jpg"},
    "zell": {"listeners": 701451, "photo": "zell.jpg"},
    "felz": {"listeners": 1039, "photo": "felz.jpg"},
    "aquafina": {"listeners": 4642, "photo": "aquafina.jpg"},
    "joven alien": {"listeners": 5584, "photo": "jovenalien.jpg"},
    "lil quenti": {"listeners": 179189, "photo": "lilquenti.jpg"},
    "leston": {"listeners": 75571, "photo": "leston.jpg"},
    "underaiki": {"listeners": 138216, "photo": "underaiki.jpg"},
    "Lolo": {"listeners": 84193, "photo": "lolo.jpg"},
    "salas flaco": {"listeners": 103389, "photo": "salasflaco.jpg"},
    "nafield": {"listeners": 1392, "photo": "nafield.jpg"},
    "swaggerman": {"listeners": 15963, "photo": "swaggerman.jpg"},
    "laurasad": {"listeners": 21113, "photo": "laurasad.jpg"},
    "kuraimokha": {"listeners": 75791, "photo": "kuraimokha.jpg"},
    "rojuu": {"listeners": 829279, "photo": "rojuu.jpg"},
    "stickyma": {"listeners": 356520, "photo": "stickyma.jpg"},
    "slappy": {"listeners": 54990, "photo": "slappy.jpg"},
    "mda": {"listeners": 147969, "photo": "mda.jpg"},
    "agusfortnite": {"listeners": 151614, "photo": "agusfortnite.jpg"},
    "stiffy": {"listeners": 224655, "photo": "stiffy.jpg"},
    "turrobaby": {"listeners": 297544, "photo": "turrobaby.jpg"},
    "orslok": {"listeners": 225671, "photo": "orslok.jpg"},
    "traw": {"listeners": 24400, "photo": "traw.jpg"},
    "oddmami": {"listeners": 106384, "photo": "oddmami.jpg"},
    "trashu": {"listeners": 31290, "photo": "trashu.jpg"},
    "bardo": {"listeners": 7132, "photo": "bardo.jpg"},
    "clutchill": {"listeners": 128482, "photo": "clutchill.jpg"},
    "agush": {"listeners": 35939, "photo": "agush.jpg"},
    "cody2077": {"listeners": 1746, "photo": "cody2077.jpg"},
    "muerejoven": {"listeners": 171448, "photo": "muerejoven.jpg"},
    "Olivia": {"listeners": 5060, "photo": "olivia.jpg"},
    "kifykify": {"listeners": 28643, "photo": "kifykify.jpg"},
    "saramalacra": {"listeners": 606265, "photo": "saramalacra.jpg"},
    "tuw4": {"listeners": 49793, "photo": "tuw4.jpg"},
    "joshu joshu": {"listeners": 33047, "photo": "joshujoshu.jpg"}
}

def format_listeners(listeners):
    """Format listener count with thousands separators"""
    return f"{listeners:,}"

def display_ad_banner(ad_id="", ad_slot="", width=320, height=100, ad_type="banner"):
    """Display Google AdSense ad with placeholder for now"""
    # Placeholder HTML for Google AdSense - you'll replace with your actual ad code
    ad_html = f"""
    <div style="
        width: {width}px;
        height: {height}px;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border: 2px dashed #dee2e6;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 20px auto;
        color: #6c757d;
        font-weight: 600;
        text-align: center;
        font-size: 14px;
    ">
        🎯 Google AdSense - {ad_type.title()}<br>
        <small>ID: {ad_id or 'Insertar tu ID aquí'}</small>
    </div>
    
    <!-- Aquí irá tu código real de Google AdSense:
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX"
         crossorigin="anonymous"></script>
    <ins class="adsbygoogle"
         style="display:inline-block;width:{width}px;height:{height}px"
         data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
         data-ad-slot="{ad_slot}"></ins>
    <script>
         (adsbygoogle = window.adsbygoogle || []).push({{}});
    </script>
    -->
    """
    
    components.html(ad_html, height=height + 50, width=width + 20)

def display_responsive_ad(ad_id="", ad_slot="", ad_type="responsive"):
    """Display responsive Google AdSense ad"""
    ad_html = f"""
    <div style="
        width: 100%;
        height: 90px;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border: 2px dashed #dee2e6;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 15px 0;
        color: #6c757d;
        font-weight: 600;
        text-align: center;
        font-size: 14px;
    ">
        📱 Google AdSense - {ad_type.title()}<br>
        <small>ID: {ad_id or 'Insertar tu ID aquí'}</small>
    </div>
    
    <!-- Aquí irá tu código real de Google AdSense responsivo:
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX"
         crossorigin="anonymous"></script>
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
         data-ad-slot="{ad_slot}"
         data-ad-format="auto"
         data-full-width-responsive="true"></ins>
    <script>
         (adsbygoogle = window.adsbygoogle || []).push({{}});
    </script>
    -->
    """
    
    components.html(ad_html, height=140)

def initialize_game():
    """Initialize or reset the game state"""
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.current_artists = None
    st.session_state.show_answer = False
    st.session_state.last_guess_correct = None

def select_random_artists():
    """Select two different random artists"""
    artist_names = list(ARTISTS.keys())
    selected = random.sample(artist_names, 2)
    return selected[0], selected[1]


def display_artist(artist_name, show_listeners=False, is_button=False):
    """Display artist information as a High or Lower style card"""
    artist_data = ARTISTS[artist_name]
    
    # Add CSS styles for the card
    st.markdown("""
    <style>
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    
    .artist-container {
        position: relative;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
        margin: 15px 0;
        overflow: hidden;
        animation: slideIn 0.6s ease-out;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .artist-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.3);
        animation: pulse 1.5s infinite;
    }
    
    .artist-name-box {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 15px;
        text-align: center;
        border-bottom: 3px solid #ff4757;
        margin: 0;
    }
    
    .artist-name {
        font-size: 22px;
        font-weight: 900;
        color: #2c3e50;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 1px;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
    }
    
    .artist-image-container {
        position: relative;
        overflow: hidden;
        display: flex;
        justify-content: center;
        background: #000;
    }
    
    .artist-listeners {
        background: rgba(0, 0, 0, 0.8);
        color: #ffffff;
        padding: 10px 15px;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
        margin: 0;
    }
    
    .artist-listeners-hidden {
        background: rgba(255, 71, 87, 0.9);
        color: #ffffff;
        padding: 10px 15px;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
        margin: 0;
    }
    
    .image-fallback {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 300px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .fallback-icon {
        font-size: 80px;
        margin-bottom: 15px;
        opacity: 0.8;
    }
    
    .fallback-text {
        color: rgba(255, 255, 255, 0.9);
        font-size: 14px;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Start the card container
    st.markdown('<div class="artist-container">', unsafe_allow_html=True)
    
    # Artist name box (encima de la imagen)
    st.markdown(f'<div class="artist-name-box"><div class="artist-name">{artist_name.title()}</div></div>', unsafe_allow_html=True)
    
    # Image container
    st.markdown('<div class="artist-image-container">', unsafe_allow_html=True)
    
    # Try to display the image, with fallback if image doesn't exist
    try:
        image_path = artist_data["photo"]
        try:
            st.image(image_path, width=300)
        except:
            try:
                st.image(f"images/{image_path}", width=300)
            except:
                st.markdown('''
                <div class="image-fallback">
                    <div class="fallback-icon">🎵</div>
                    <div class="fallback-text">Imagen no encontrada</div>
                </div>
                ''', unsafe_allow_html=True)
    except:
        st.markdown('''
        <div class="image-fallback">
            <div class="fallback-icon">🎵</div>
            <div class="fallback-text">Imagen no encontrada</div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close image container
    
    # Listener count
    if show_listeners:
        st.markdown(f'<div class="artist-listeners">{format_listeners(artist_data["listeners"])} oyentes mensuales</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="artist-listeners-hidden">??? oyentes mensuales</div>', unsafe_allow_html=True)
    
    # Close the card container
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    # Load background image
    import base64
    try:
        with open("fondo.png", "rb") as f:
            img_data = f.read()
        img_base64 = base64.b64encode(img_data).decode()
        background_css = f"""
        /* Background styling */
        .stApp {{
            background: url('data:image/png;base64,{img_base64}') no-repeat center center fixed;
            background-size: cover;
        }}
        
        .stApp::before {{
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255, 255, 255, 0.85);
            z-index: -1;
        }}
        """
    except FileNotFoundError:
        background_css = """
        /* No background available */
        .stApp {
            background: #f8f9fa;
        }
        """
    
    # Custom CSS with background
    st.markdown("""
    <style>
    """ + background_css + """
    
    .main-title {
        font-size: 52px;
        font-weight: 900;
        text-align: center;
        color: #ffffff;
        margin-bottom: 8px;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.8);
        letter-spacing: 2px;
    }
    .subtitle {
        font-size: 18px;
        text-align: center;
        color: #ffffff;
        margin-bottom: 15px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        font-weight: 600;
    }
    .vs-text {
        font-size: 42px;
        font-weight: 900;
        text-align: center;
        color: #ff4757;
        margin-top: 150px;
        padding: 10px 0;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.8);
        letter-spacing: 4px;
        transition: all 0.5s ease;
    }
    
    .vs-correct {
        font-size: 60px;
        color: #28a745;
        text-shadow: 0 0 20px rgba(40, 167, 69, 0.7);
        animation: correctPulse 1s ease-in-out;
    }
    
    .vs-wrong {
        font-size: 60px;
        color: #dc3545;
        text-shadow: 0 0 20px rgba(220, 53, 69, 0.7);
        animation: wrongShake 0.8s ease-in-out;
    }
    
    @keyframes correctPulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.3); }
        100% { transform: scale(1); }
    }
    
    @keyframes wrongShake {
        0%, 100% { transform: translateX(0); }
        20%, 60% { transform: translateX(-10px) rotate(-5deg); }
        40%, 80% { transform: translateX(10px) rotate(5deg); }
    }
    .score-display {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
        margin: 10px 0;
        background: rgba(0, 0, 0, 0.6);
        padding: 8px 20px;
        border-radius: 20px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);
        display: inline-block;
    }
    .score-container {
        text-align: center;
        margin: 15px 0;
    }
    
    /* Compact layout styles */
    .stApp > div {
        padding-top: 1rem;
    }
    
    /* Make artist cards more compact */
    .artist-card {
        margin-bottom: 10px !important;
    }
    
    /* Reduce spacing in main container */
    .main > div {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    /* Make columns more compact */
    [data-testid="column"] {
        padding: 0 0.5rem;
    }
    
    /* Fixed image size 300x300 */
    .stImage img {
        width: 300px !important;
        height: 300px !important;
        object-fit: cover !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
    }
    .stButton > button {
        background: linear-gradient(135deg, #ff4757, #ff3838);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 18px 25px;
        font-size: 16px;
        font-weight: 900;
        width: 100%;
        height: 65px;
        margin: 8px 0;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 6px 20px rgba(255, 71, 87, 0.4);
        text-transform: uppercase;
        letter-spacing: 1px;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #ff3838, #ff4757);
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(255, 71, 87, 0.6);
    }
    .stButton > button:active {
        transform: translateY(-1px);
        box-shadow: 0 4px 15px rgba(255, 71, 87, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="main-title">🎵 HIGH OR LOWER</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Artistas Underground de Argentina</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">¿Quién tiene más oyentes mensuales en Spotify?</div>', unsafe_allow_html=True)
    
    # Initialize session state variables
    if 'score' not in st.session_state:
        initialize_game()
    
    # Header Ad - Top banner
    display_responsive_ad(ad_type="header banner")
    
    # Show current score prominently
    st.markdown(f'<div class="score-container"><div class="score-display">Puntaje: {st.session_state.score}</div></div>', unsafe_allow_html=True)
    
    # Game over state
    if st.session_state.game_over:
        st.markdown('<div style="background-color: #dc3545; color: white; padding: 20px; border-radius: 10px; text-align: center; font-size: 24px; font-weight: bold; margin: 20px 0;">¡GAME OVER! 💀</div>', unsafe_allow_html=True)
        
        if st.session_state.current_artists:
            artist1, artist2 = st.session_state.current_artists
            
            st.markdown("### Resultados Finales")
            col1, col2, col3 = st.columns([5, 1, 5])
            
            with col1:
                display_artist(artist1, show_listeners=True)
                
            with col2:
                st.markdown('<div class="vs-text">VS</div>', unsafe_allow_html=True)
                
            with col3:
                display_artist(artist2, show_listeners=True)
            
            # Show which had more listeners
            listeners1 = ARTISTS[artist1]["listeners"]
            listeners2 = ARTISTS[artist2]["listeners"]
            winner = artist1 if listeners1 > listeners2 else artist2
            st.markdown(f'<div style="background-color: #28a745; color: white; padding: 15px; border-radius: 10px; text-align: center; font-size: 20px; font-weight: bold; margin: 20px 0;">¡**{winner.title()}** tenía más oyentes!</div>', unsafe_allow_html=True)
        
        st.markdown(f'<div class="score-display" style="color: #dc3545;">Tu Puntaje Final: {st.session_state.score}</div>', unsafe_allow_html=True)
        
        # Game Over Ad - Rectangle banner
        display_ad_banner(width=300, height=250, ad_type="game over")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🎮 Jugar de Nuevo", type="primary", use_container_width=True):
                initialize_game()
                st.rerun()
        
        return
    

    # Select new artists if needed
    if st.session_state.current_artists is None:
        st.session_state.current_artists = select_random_artists()
        st.session_state.show_answer = False
    
    artist1, artist2 = st.session_state.current_artists
    
    # Mid-content Ad - Every 3 points
    if st.session_state.score > 0 and st.session_state.score % 3 == 0:
        display_responsive_ad(ad_type="mid-content")
    
    # Display the two artists in a vs format
    col1, col2, col3 = st.columns([5, 1, 5])
    
    with col1:
        display_artist(artist1)
        if st.button(f"⬆️ {artist1.title()} TIENE MÁS", key="artist1", type="primary", use_container_width=True):
            # Check if guess is correct
            listeners1 = ARTISTS[artist1]["listeners"]
            listeners2 = ARTISTS[artist2]["listeners"]
            
            if listeners1 > listeners2:
                st.session_state.score += 1
                st.session_state.last_guess_correct = True
                # Select new artists for next round
                st.session_state.current_artists = select_random_artists()
                st.balloons()
                st.markdown('<div style="background: linear-gradient(135deg, #28a745, #20c997); color: white; padding: 15px; border-radius: 15px; text-align: center; font-size: 20px; font-weight: bold; margin: 20px 0; box-shadow: 0 4px 15px rgba(40, 167, 69, 0.3);">🎉 ¡CORRECTO! +1 PUNTO</div>', unsafe_allow_html=True)
                st.rerun()
            else:
                st.session_state.game_over = True
                st.session_state.last_guess_correct = False
                st.rerun()

    with col2:
        st.markdown('<div class="vs-text">VS</div>', unsafe_allow_html=True)
    
    with col3:
        display_artist(artist2)
        if st.button(f"⬆️ {artist2.title()} TIENE MÁS", key="artist2", type="primary", use_container_width=True):
            # Check if guess is correct
            listeners1 = ARTISTS[artist1]["listeners"]
            listeners2 = ARTISTS[artist2]["listeners"]
            
            if listeners2 > listeners1:
                st.session_state.score += 1
                st.session_state.last_guess_correct = True
                # Select new artists for next round
                st.session_state.current_artists = select_random_artists()
                st.balloons()
                st.markdown('<div style="background: linear-gradient(135deg, #28a745, #20c997); color: white; padding: 15px; border-radius: 15px; text-align: center; font-size: 20px; font-weight: bold; margin: 20px 0; box-shadow: 0 4px 15px rgba(40, 167, 69, 0.3);">🎉 ¡CORRECTO! +1 PUNTO</div>', unsafe_allow_html=True)
                st.rerun()
            else:
                st.session_state.game_over = True
                st.session_state.last_guess_correct = False
                st.rerun()
    
    # Game instructions with better contrast
    st.markdown('<hr style="border: 1px solid rgba(255, 255, 255, 0.3); margin: 30px 0;">', unsafe_allow_html=True)
    st.markdown('<div style="background: rgba(0, 0, 0, 0.7); color: white; padding: 15px; border-radius: 10px; text-align: center; margin: 20px 0; border: 1px solid rgba(255, 255, 255, 0.2);"><strong>Cómo jugar:</strong> Haz clic en el artista que crees que tiene más oyentes mensuales en Spotify. ¡Si aciertas sumas puntos, si fallas se termina el juego!</div>', unsafe_allow_html=True)
    
    # Bottom Ad - Footer banner
    display_ad_banner(width=728, height=90, ad_type="footer")
    
    # Reset game button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Reiniciar Juego", type="secondary", use_container_width=True):
            initialize_game()
            st.rerun()
    
    # Fixed Instagram link
    st.markdown(
        """
        <div style="
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 8px 15px;
            border-radius: 25px;
            z-index: 1000;
            border: 1px solid #ff4757;
            backdrop-filter: blur(10px);
            font-size: 14px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        ">
            📱 <a href="https://www.instagram.com/j040.fr/" target="_blank" style="color: #e1306c; text-decoration: none; font-weight: bold;">@j040.fr</a>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Footer with better contrast
    st.markdown('<hr style="border: 1px solid rgba(255, 255, 255, 0.3); margin: 30px 0;">', unsafe_allow_html=True)
    st.markdown('<div style="background: rgba(0, 0, 0, 0.6); color: white; padding: 15px; border-radius: 10px; text-align: center; margin: 20px 0;">¿Te gusta el juego? Follow o vendrá la popo 👀</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
