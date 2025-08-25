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
    """Display artist information as a clean card with photo and optional listener count"""
    artist_data = ARTISTS[artist_name]
    
    # Add CSS styles for the card
    st.markdown("""
    <style>
    .artist-card {
        text-align: center;
        padding: 20px;
        border-radius: 15px;
        background-color: #f9f9f9;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    .artist-card:hover {
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        border-color: #007bff;
    }
    .artist-name {
        font-size: 24px;
        font-weight: bold;
        margin-top: 15px;
        margin-bottom: 8px;
        color: #1a1a1a;
    }
    .artist-listeners {
        font-size: 16px;
        color: #666;
        margin-top: 5px;
        font-weight: 500;
    }
    .artist-listeners-hidden {
        font-size: 16px;
        color: #999;
        margin-top: 5px;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Start the card container
    st.markdown('<div class="artist-card">', unsafe_allow_html=True)
    
    # Try to display the image, with fallback if image doesn't exist
    try:
        # Check both root directory and images/ directory
        image_path = artist_data["photo"]
        try:
            st.image(image_path, width=200, use_container_width=True)
        except:
            try:
                st.image(f"images/{image_path}", width=200, use_container_width=True)
            except:
                st.markdown('<div style="font-size: 60px; margin: 20px 0;">🎵</div>', unsafe_allow_html=True)
                st.markdown('<div style="color: #6c757d; font-size: 14px;">(Imagen no encontrada)</div>', unsafe_allow_html=True)
    except:
        st.markdown('<div style="font-size: 60px; margin: 20px 0;">🎵</div>', unsafe_allow_html=True)
        st.markdown('<div style="color: #6c757d; font-size: 14px;">(Imagen no encontrada)</div>', unsafe_allow_html=True)
    
    # Artist name
    st.markdown(f'<div class="artist-name">{artist_name.title()}</div>', unsafe_allow_html=True)
    
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
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        color: #1f1f23;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 24px;
        text-align: center;
        color: #6c757d;
        margin-bottom: 30px;
    }
    .vs-text {
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        color: #007bff;
        margin: 20px 0;
    }
    .score-display {
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        color: #28a745;
        margin: 20px 0;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 15px 25px;
        font-size: 18px;
        font-weight: bold;
        width: 100%;
        height: 60px;
        margin: 15px 0;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
    .stButton > button:active {
        transform: translateY(0px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
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
    st.markdown(f'<div class="score-display">Puntaje: {st.session_state.score}</div>', unsafe_allow_html=True)
    
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
    
    # Game instructions
    st.markdown("---")
    st.markdown("**Cómo jugar:** Haz clic en el artista que crees que tiene más oyentes mensuales en Spotify. ¡Si aciertas sumas puntos, si fallas se termina el juego!")
    
    # Bottom Ad - Footer banner
    display_ad_banner(width=728, height=90, ad_type="footer")
    
    # Reset game button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Reiniciar Juego", type="secondary", use_container_width=True):
            initialize_game()
            st.rerun()
    
    # Footer with Instagram contact
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; padding: 20px; color: #6c757d;">
            <p>¿Te gusta el juego? 📱 <strong>Sígueme en Instagram:</strong> 
            <a href="https://www.instagram.com/j040.fr/" target="_blank" style="color: #e1306c; text-decoration: none; font-weight: bold;">@j040.fr</a></p>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
