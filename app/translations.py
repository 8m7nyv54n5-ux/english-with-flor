# app/translations.py
# Contains all user-facing text for the site in both English and Spanish.
# TRANSLATIONS is a nested dictionary: TRANSLATIONS["en"]["key"] or TRANSLATIONS["es"]["key"].
# Routes pass the correct language dictionary to templates as the variable `t`,
# so templates just use {{ t.some_key }} without needing to know the language.

TRANSLATIONS = {
    "en": {
        # Navigation
        "nav_home": "Home",
        "nav_courses": "Courses",
        "nav_about": "About",
        "nav_contact": "Contact",
        "nav_register": "Register",
        "nav_login": "Login",
        "nav_dashboard": "My Account",

        # Home — hero
        "home_title": "Speak English with confidence",
        "home_subtitle": "Immersive, conversation-first English courses designed around how you actually learn — not how textbooks think you do.",
        "hero_tag": "Now enrolling for 2026",
        "hero_cta_primary": "Start your journey →",
        "hero_cta_secondary": "Explore courses",

        # Home — stats
        "stat_students": "Students enrolled",
        "stat_years": "Years of experience",
        "stat_format": "1-to-1 & small groups",
        "stat_rating": "Average rating",

        # Home — method
        "method_label": "Our Method",
        "method_title": "Learning that actually sticks",
        "method_desc": "We ditched the textbook-first approach. Our method is built on how the brain naturally acquires language — through context, conversation, and confidence.",
        "step1_title": "Immerse & Listen",
        "step1_desc": "Start with real conversations and stories — your brain absorbs patterns before rules.",
        "step2_title": "Practice & Speak",
        "step2_desc": "Regular conversation sessions focused on your goals. Mistakes are celebrated — they mean you are trying.",
        "step3_title": "Refine & Master",
        "step3_desc": "Targeted feedback and personalised exercises lock in what you have learned for permanent recall.",

        # Home — student stories section label
        "stories_label": "Student Stories",

        # Home — CTA
        "cta_title": "Book your level test",
        "cta_desc": "Not sure where to start? Take a level test with Flor and find out exactly where you are — and where you could go.",
        "cta_btn": "Book your test now →",
        # WhatsApp link — replace 0000000000 with Flor's number (international format, no dashes)
        "whatsapp_url": "https://wa.me/0000000000?text=Hi%20Flor%2C%20I%27d%20like%20to%20book%20a%20level%20test",

        # Footer
        "footer_copy": "© 2026 English with Flor. All rights reserved.",

        # Courses — listing page
        "courses_title": "Our Courses",
        "course_name": "English for All Levels",
        "course_desc": "Whether you are a complete beginner or looking to polish your fluency, our English course is tailored to you. Classes are available one-to-one or in small groups.",

        "courses_intro": "Choose the level that fits where you are today. Every course is taught in small groups or one-to-one, so you get real attention — not just a seat in a class.",
        "courses_view_btn": "View course →",

        # A1 course
        "a1_title": "A1 English",
        "a1_level": "A1",
        "a1_tagline": "Your English journey starts here — from the very first word.",
        "a1_who_title": "Who is this for?",
        "a1_who_desc": "Complete beginners with little or no English. You may know a few words but have never had structured lessons. This course gives you a solid, confidence-building foundation from day one — no experience needed, just curiosity.",
        "a1_learn_title": "What you will learn",
        "a1_learn_items": [
            "Introduce yourself and talk about where you are from",
            "Use basic greetings, numbers, colours, and everyday vocabulary",
            "Ask and answer simple questions about people and places",
            "Understand very short, clear spoken and written English",
            "Build the confidence to say something — anything — in English",
        ],
        "a1_format_title": "Format & schedule",
        "a1_format_desc": "Two 60-minute sessions per week, available mornings or evenings. One-to-one with Flor or a small group of up to 4 students.",
        "a1_price_title": "Pricing",
        "a1_price_desc": "From $75 USD / month for group classes · $140 USD / month one-to-one. Includes all materials and a monthly progress review.",
        "a1_cta": "Enrol in A1 →",
        "a1_back": "← Back to all courses",

        # A2 course
        "a2_title": "A2 English",
        "a2_level": "A2",
        "a2_tagline": "Move beyond basics and handle everyday English with ease.",
        "a2_who_title": "Who is this for?",
        "a2_who_desc": "You know some English but struggle in real situations — ordering food, filling in forms, chatting with colleagues. This course bridges the gap between knowing words and actually using them.",
        "a2_learn_title": "What you will learn",
        "a2_learn_items": [
            "Talk about your daily routine, family, work, and interests",
            "Handle common situations: shopping, travel, appointments",
            "Understand short, simple texts and conversations",
            "Write basic messages and emails",
            "Start forming opinions and expressing simple preferences",
        ],
        "a2_format_title": "Format & schedule",
        "a2_format_desc": "Two 60-minute sessions per week, available mornings or evenings. One-to-one with Flor or a small group of up to 4 students.",
        "a2_price_title": "Pricing",
        "a2_price_desc": "From $75 USD / month for group classes · $140 USD / month one-to-one. Includes all materials and a monthly progress review.",
        "a2_cta": "Enrol in A2 →",
        "a2_back": "← Back to all courses",

        # B1 course
        "b1_title": "B1 English",
        "b1_level": "B1",
        "b1_tagline": "Speak in the real world — at work, travelling, and beyond.",
        "b1_who_title": "Who is this for?",
        "b1_who_desc": "You can get by in English but lack confidence when things go off-script. This level focuses on fluency in genuine, unpredictable situations — the kind you actually encounter.",
        "b1_learn_title": "What you will learn",
        "b1_learn_items": [
            "Discuss plans, opinions, and past experiences in natural English",
            "Handle most travel and workplace situations confidently",
            "Understand the main points of clear, standard speech",
            "Write clear, connected messages and short texts",
            "Express yourself without long pauses or switching to Spanish",
        ],
        "b1_format_title": "Format & schedule",
        "b1_format_desc": "Two 75-minute sessions per week. One-to-one or small group available.",
        "b1_price_title": "Pricing",
        "b1_price_desc": "From $90 USD / month for group classes · $165 USD / month one-to-one. Includes all materials and a monthly progress review.",
        "b1_cta": "Enrol in B1 →",
        "b1_back": "← Back to all courses",

        # B2 course
        "b2_title": "B2 English",
        "b2_level": "B2",
        "b2_tagline": "Reach the level where English stops feeling like an effort.",
        "b2_who_title": "Who is this for?",
        "b2_who_desc": "You communicate well but native speakers still catch you out — fast speech, idioms, complex topics. B2 is where fluency becomes real and English stops requiring conscious effort.",
        "b2_learn_title": "What you will learn",
        "b2_learn_items": [
            "Discuss complex, abstract topics with clarity and confidence",
            "Understand native speakers at natural speed, including accents",
            "Write detailed emails, reports, and structured arguments",
            "Use a wide range of vocabulary naturally and accurately",
            "Interact spontaneously without searching for words",
        ],
        "b2_format_title": "Format & schedule",
        "b2_format_desc": "Two 75-minute sessions per week. Focus on conversation, debate, and writing. One-to-one or small group available.",
        "b2_price_title": "Pricing",
        "b2_price_desc": "From $90 USD / month for group classes · $165 USD / month one-to-one. Includes all materials and a monthly progress review.",
        "b2_cta": "Enrol in B2 →",
        "b2_back": "← Back to all courses",

        # C1 course (hidden behind SHOW_C_LEVELS feature flag)
        "c1_title": "C1 English",
        "c1_level": "C1",
        "c1_tagline": "Communicate with the precision and confidence of a near-native speaker.",
        "c1_who_title": "Who is this for?",
        "c1_who_desc": "Fluent speakers who need English to perform at a high level — presenting to international clients, writing professionally, or navigating complex social situations without ever feeling limited by their language.",
        "c1_learn_title": "What you will learn",
        "c1_learn_items": [
            "Express nuanced ideas clearly and persuasively",
            "Understand demanding texts and implicit meaning",
            "Produce well-structured writing at a professional or academic standard",
            "Handle challenging conversations, negotiations, and presentations",
            "Refine and eliminate deeply ingrained errors",
        ],
        "c1_format_title": "Format & schedule",
        "c1_format_desc": "One or two flexible sessions per week. One-to-one only at this level.",
        "c1_price_title": "Pricing",
        "c1_price_desc": "From $180 USD / month one-to-one. Fully tailored curriculum.",
        "c1_cta": "Enrol in C1 →",
        "c1_back": "← Back to all courses",

        # C2 course (hidden behind SHOW_C_LEVELS feature flag)
        "c2_title": "C2 English",
        "c2_level": "C2",
        "c2_tagline": "The highest level — English as precise and powerful as your own language.",
        "c2_who_title": "Who is this for?",
        "c2_who_desc": "Near-native speakers who want to close the final gap. Perfect for professionals publishing in English, academics writing internationally, or anyone who refuses to settle for \"very good\" when \"excellent\" is within reach.",
        "c2_learn_title": "What you will learn",
        "c2_learn_items": [
            "Understand virtually everything — spoken or written, any accent",
            "Summarise and synthesise complex information from multiple sources",
            "Write with elegance, subtlety, and stylistic control",
            "Use humour, irony, and cultural references like a native",
            "Achieve complete fluency with no observable gaps",
        ],
        "c2_format_title": "Format & schedule",
        "c2_format_desc": "Fully flexible and highly personalised. One-to-one only.",
        "c2_price_title": "Pricing",
        "c2_price_desc": "From $200 USD / month one-to-one. Custom programme built around your specific goals.",
        "c2_cta": "Enrol in C2 →",
        "c2_back": "← Back to all courses",

        # About
        "about_title": "About Us",
        "about_meet_title": "Meet Flor",
        "about_meet_body": "Hi! I'm Flor, a qualified English teacher based in Argentina. I've been helping students of all ages and levels improve their English for over 10 years. Whether you're preparing for an exam, need English for work, or simply want to feel more confident speaking — I'm here to help.",
        "about_approach_title": "My Approach",
        "about_approach_body": "I believe the best way to learn a language is by using it. My classes focus on real conversation, practical vocabulary, and building confidence from day one. Every student is different, so I adapt each lesson to your goals, your level, and your pace.",
        "about_why_title": "Why Choose English with Flor?",
        "about_why_1": "Personalised lessons tailored to your goals and level",
        "about_why_2": "Flexible scheduling — classes fit around your life",
        "about_why_3": "A supportive, relaxed environment where mistakes are welcome",
        "about_why_4": "Experience with students from Argentina and around the world",
        "about_cta": "Get in Touch",

        # Contact
        "contact_title": "Contact Us",
        "contact_email": "Email",
        "contact_phone": "Phone",
        "contact_name_label": "Your Name",
        "contact_email_label": "Your Email",
        "contact_message_label": "Your Message",
        "contact_submit": "Send Message",
        "contact_success": "Thanks for your message! We'll get back to you soon.",
        "contact_whatsapp_btn": "Or chat with Flor on WhatsApp →",
        "contact_whatsapp_url": "https://wa.me/0000000000?text=Hi%20Flor%2C%20I%20sent%20a%20message%20via%20the%20website",
        "error_message_length": "Message must be between 10 and 2000 characters.",

        # Register — page text
        "register_title": "Create an Account",
        "already_have_account": "Already have an account?",
        "login_link": "Log in here",

        # Register — field labels
        "register_first_name": "First Name",
        "register_last_name": "Last Name",
        "register_email": "Email",
        "register_username": "Username",
        "register_password": "Password",
        "register_confirm": "Confirm Password",
        "register_submit": "Register",

        # Register — validator error messages (keys match message= strings in forms.py)
        "error_field_required": "This field is required.",
        "error_name_length": "Must be at least 2 characters.",
        "error_username_length": "Must be between 3 and 80 characters.",
        "error_invalid_email": "Please enter a valid email address.",
        "error_password_too_short": "Password must be at least 8 characters.",
        "error_passwords_must_match": "Passwords must match.",

        # Login
        "login_title": "Log In",
        "no_account": "Don't have an account?",
        "register_link": "Register here",
        "logout": "Log Out",

        # Enrolment
        "enrol_title": "Enrol on a Course",

        # Enrolment form — address fields
        "enrol_address_title":   "Your Address",
        "enrol_address_line":    "Street address",
        "enrol_city":            "City",
        "enrol_province":        "Province / State",
        "enrol_country":         "Country",
        "enrol_postcode":        "Postcode / ZIP",

        # Word of the day
        "wotd_label": "Word of the Day",
        "wotd_no_equiv": "No direct Spanish equivalent",

        # Dashboard
        "dashboard_title": "Welcome",
        "dashboard_your_details": "Your Details",
        "dashboard_username": "Username",
        "dashboard_email": "Email",
        "dashboard_enrolment": "Your Enrolment",
        "dashboard_course": "Course",
        "dashboard_passport": "Passport Number",
        "dashboard_not_enrolled": "You are not yet enrolled on a course.",
        "dashboard_enrol_link": "Enrol now",

        # Dashboard — edit profile
        "edit_profile_title": "Edit Your Details",
        "edit_profile_first_name": "First Name",
        "edit_profile_last_name": "Last Name",
        "edit_profile_email": "Email",
        "edit_profile_submit": "Save Changes",
        "edit_profile_success": "Your details have been updated.",
        "edit_profile_btn": "Edit Details",
        "edit_profile_cancel": "Cancel",

        # Dashboard — edit address
        "edit_address_title":   "Edit Your Address",
        "edit_address_submit":  "Save Changes",
        "edit_address_success": "Your address has been updated.",
        "edit_address_btn":     "Edit Address",
        "edit_address_cancel":  "Cancel",

        # Dashboard — change password
        "change_pw_title": "Change Your Password",
        "change_pw_current": "Current Password",
        "change_pw_new": "New Password",
        "change_pw_confirm": "Confirm New Password",
        "change_pw_submit": "Change Password",
        "change_pw_success": "Your password has been changed.",
        "change_pw_btn": "Change Password",
        "change_pw_cancel": "Cancel",
        "error_wrong_password": "Current password is incorrect.",

        # Dashboard — delete account
        "delete_account_title": "Delete Your Account",
        "delete_account_warning": "This action is permanent. Your account, personal details, and enrolment will be deleted immediately. This cannot be undone.",
        "delete_account_password": "Enter your password to confirm",
        "delete_account_submit": "Delete My Account",
        "delete_account_success": "Your account has been deleted.",
        "delete_account_btn": "Delete Account",
        "delete_account_cancel": "Cancel",

        # Errors
        "error_username_taken": "That username is already taken. Please choose another.",
        "error_email_taken": "An account with that email already exists.",
        "error_invalid_credentials": "Invalid username or password. Please try again.",
        "error_argentina_fields": "Please enter both your CUIT/CUIL and DNI.",
        "error_passport_required": "Please enter your passport number.",
        "error_address_length":  "Street address must be 200 characters or fewer.",
        "error_city_length":     "City must be 100 characters or fewer.",
        "error_province_length": "Province / State must be 100 characters or fewer.",
        "error_country_length":  "Country must be 100 characters or fewer.",
        "error_postcode_length": "Postcode / ZIP must be 20 characters or fewer.",

        # Error pages
        "error_404_title": "Page Not Found",
        "error_404_message": "Sorry, the page you are looking for does not exist or has been moved.",
        "error_500_title": "Something Went Wrong",
        "error_500_message": "We are having some technical difficulties. Please try again later.",
        "error_go_home": "Go to Home Page",
    },
    "es": {
        # Navigation
        "nav_home": "Inicio",
        "nav_courses": "Cursos",
        "nav_about": "Quiénes somos",
        "nav_contact": "Contacto",
        "nav_register": "Registrarse",
        "nav_login": "Iniciar sesión",
        "nav_dashboard": "Mi cuenta",

        # Home — hero
        "home_title": "Habla inglés con confianza",
        "home_subtitle": "Cursos de inglés conversacionales e inmersivos, diseñados para cómo realmente aprendes — no como los libros de texto creen que lo haces.",
        "hero_tag": "Inscripciones abiertas 2026",
        "hero_cta_primary": "Empieza tu camino →",
        "hero_cta_secondary": "Ver cursos",

        # Home — stats
        "stat_students": "Estudiantes inscritos",
        "stat_years": "Años de experiencia",
        "stat_format": "Individual y grupos pequeños",
        "stat_rating": "Valoración media",

        # Home — method
        "method_label": "Nuestro método",
        "method_title": "Un aprendizaje que realmente funciona",
        "method_desc": "Olvidamos el enfoque basado en libros de texto. Nuestro método se basa en cómo el cerebro adquiere el lenguaje de forma natural — a través del contexto, la conversación y la confianza.",
        "step1_title": "Sumérgete y escucha",
        "step1_desc": "Empieza con conversaciones reales e historias — tu cerebro absorbe patrones antes que reglas.",
        "step2_title": "Practica y habla",
        "step2_desc": "Sesiones de conversación regulares enfocadas en tus objetivos. Los errores se celebran — significan que lo estás intentando.",
        "step3_title": "Perfecciona y domina",
        "step3_desc": "Retroalimentación personalizada y ejercicios específicos consolidan lo aprendido para un recuerdo permanente.",

        # Home — student stories section label
        "stories_label": "Lo que dicen nuestros alumnos",

        # Home — CTA
        "cta_title": "Reserva tu test de nivel",
        "cta_desc": "¿No sabes por dónde empezar? Haz un test de nivel con Flor y descubre exactamente dónde estás — y hasta dónde puedes llegar.",
        "cta_btn": "Reserva tu test ahora →",
        # WhatsApp link — replace 0000000000 with Flor's number (international format, no dashes)
        "whatsapp_url": "https://wa.me/0000000000?text=Hola%20Flor%2C%20me%20gustar%C3%ADa%20reservar%20un%20test%20de%20nivel",

        # Footer
        "footer_copy": "© 2026 English with Flor. Todos los derechos reservados.",

        # Courses — listing page
        "courses_title": "Nuestros cursos",
        "course_name": "Inglés para todos los niveles",
        "course_desc": "Tanto si eres principiante como si quieres perfeccionar tu fluidez, nuestro curso de inglés se adapta a ti. Las clases están disponibles de forma individual o en grupos pequeños.",

        "courses_intro": "Elige el nivel que se adapta a dónde estás hoy. Cada curso se imparte en grupos pequeños o de forma individual, para que recibas atención real.",
        "courses_view_btn": "Ver curso →",

        # A1 course
        "a1_title": "Inglés A1",
        "a1_level": "A1",
        "a1_tagline": "Tu camino en inglés empieza aquí — desde la primera palabra.",
        "a1_who_title": "¿Para quién es este curso?",
        "a1_who_desc": "Principiantes absolutos con poco o ningún inglés. Puede que conozcas algunas palabras pero nunca hayas tenido clases estructuradas. Este curso te da una base sólida desde el primer día — sin experiencia previa, solo curiosidad.",
        "a1_learn_title": "Qué aprenderás",
        "a1_learn_items": [
            "Presentarte y hablar sobre de dónde eres",
            "Usar saludos básicos, números, colores y vocabulario cotidiano",
            "Hacer y responder preguntas simples sobre personas y lugares",
            "Entender inglés oral y escrito muy corto y claro",
            "Ganar la confianza para decir algo — lo que sea — en inglés",
        ],
        "a1_format_title": "Formato y horario",
        "a1_format_desc": "Dos sesiones de 60 minutos por semana, disponibles por las mañanas o por las tardes. Individual con Flor o grupo de hasta 4 estudiantes.",
        "a1_price_title": "Precio",
        "a1_price_desc": "Desde $75 USD / mes en grupo · $140 USD / mes individual. Incluye todos los materiales y una revisión mensual de progreso.",
        "a1_cta": "Inscribirse en A1 →",
        "a1_back": "← Volver a todos los cursos",

        # A2 course
        "a2_title": "Inglés A2",
        "a2_level": "A2",
        "a2_tagline": "Supera lo básico y maneja el inglés cotidiano con facilidad.",
        "a2_who_title": "¿Para quién es este curso?",
        "a2_who_desc": "Sabes algo de inglés pero te cuesta en situaciones reales — pedir comida, rellenar formularios, charlar con compañeros. Este curso cierra la brecha entre saber palabras y realmente usarlas.",
        "a2_learn_title": "Qué aprenderás",
        "a2_learn_items": [
            "Hablar sobre tu rutina diaria, familia, trabajo e intereses",
            "Manejarte en situaciones comunes: compras, viajes, citas",
            "Entender textos y conversaciones cortos y sencillos",
            "Escribir mensajes y correos básicos",
            "Empezar a expresar opiniones y preferencias simples",
        ],
        "a2_format_title": "Formato y horario",
        "a2_format_desc": "Dos sesiones de 60 minutos por semana, disponibles por las mañanas o por las tardes. Individual con Flor o grupo de hasta 4 estudiantes.",
        "a2_price_title": "Precio",
        "a2_price_desc": "Desde $75 USD / mes en grupo · $140 USD / mes individual. Incluye todos los materiales y una revisión mensual de progreso.",
        "a2_cta": "Inscribirse en A2 →",
        "a2_back": "← Volver a todos los cursos",

        # B1 course
        "b1_title": "Inglés B1",
        "b1_level": "B1",
        "b1_tagline": "Habla en el mundo real — en el trabajo, viajando y más allá.",
        "b1_who_title": "¿Para quién es este curso?",
        "b1_who_desc": "Te defiendes en inglés pero te falta confianza cuando las cosas se salen del guion. Este nivel se enfoca en la fluidez en situaciones reales e impredecibles — las que realmente encuentras.",
        "b1_learn_title": "Qué aprenderás",
        "b1_learn_items": [
            "Hablar de planes, opiniones y experiencias pasadas en inglés natural",
            "Manejarte con confianza en la mayoría de situaciones de viaje y trabajo",
            "Entender los puntos principales de un discurso claro y estándar",
            "Escribir mensajes claros y textos cortos bien conectados",
            "Expresarte sin largas pausas ni cambiar al español",
        ],
        "b1_format_title": "Formato y horario",
        "b1_format_desc": "Dos sesiones de 75 minutos por semana. Disponible individual o en grupo pequeño.",
        "b1_price_title": "Precio",
        "b1_price_desc": "Desde $90 USD / mes en grupo · $165 USD / mes individual. Incluye todos los materiales y una revisión mensual de progreso.",
        "b1_cta": "Inscribirse en B1 →",
        "b1_back": "← Volver a todos los cursos",

        # B2 course
        "b2_title": "Inglés B2",
        "b2_level": "B2",
        "b2_tagline": "Alcanza el nivel en el que el inglés deja de requerir esfuerzo.",
        "b2_who_title": "¿Para quién es este curso?",
        "b2_who_desc": "Te comunicas bien pero los hablantes nativos todavía te pillan desprevenido — habla rápida, expresiones idiomáticas, temas complejos. B2 es donde la fluidez se vuelve real y el inglés deja de requerir esfuerzo consciente.",
        "b2_learn_title": "Qué aprenderás",
        "b2_learn_items": [
            "Hablar de temas complejos y abstractos con claridad y confianza",
            "Entender a hablantes nativos a velocidad natural, incluyendo acentos",
            "Escribir correos detallados, informes y argumentos estructurados",
            "Usar una amplia gama de vocabulario de forma natural y precisa",
            "Interactuar espontáneamente sin buscar las palabras",
        ],
        "b2_format_title": "Formato y horario",
        "b2_format_desc": "Dos sesiones de 75 minutos por semana. Enfocadas en conversación, debate y escritura. Individual o grupo pequeño.",
        "b2_price_title": "Precio",
        "b2_price_desc": "Desde $90 USD / mes en grupo · $165 USD / mes individual. Incluye todos los materiales y una revisión mensual de progreso.",
        "b2_cta": "Inscribirse en B2 →",
        "b2_back": "← Volver a todos los cursos",

        # C1 course (hidden behind SHOW_C_LEVELS feature flag)
        "c1_title": "Inglés C1",
        "c1_level": "C1",
        "c1_tagline": "Comunícate con la precisión y confianza de un hablante casi nativo.",
        "c1_who_title": "¿Para quién es este curso?",
        "c1_who_desc": "Hablantes fluidos que necesitan el inglés para rendir a un nivel alto — presentar a clientes internacionales, escribir profesionalmente, o moverse en situaciones sociales complejas sin sentirse limitados por el idioma.",
        "c1_learn_title": "Qué aprenderás",
        "c1_learn_items": [
            "Expresar ideas con matiz de forma clara y persuasiva",
            "Entender textos exigentes y significados implícitos",
            "Producir escritura bien estructurada a nivel profesional o académico",
            "Manejar conversaciones, negociaciones y presentaciones desafiantes",
            "Eliminar y pulir errores profundamente arraigados",
        ],
        "c1_format_title": "Formato y horario",
        "c1_format_desc": "Una o dos sesiones flexibles por semana. Solo individual a este nivel.",
        "c1_price_title": "Precio",
        "c1_price_desc": "Desde $180 USD / mes individual. Programa completamente personalizado.",
        "c1_cta": "Inscribirse en C1 →",
        "c1_back": "← Volver a todos los cursos",

        # C2 course (hidden behind SHOW_C_LEVELS feature flag)
        "c2_title": "Inglés C2",
        "c2_level": "C2",
        "c2_tagline": "El nivel más alto — inglés tan preciso y poderoso como tu propio idioma.",
        "c2_who_title": "¿Para quién es este curso?",
        "c2_who_desc": "Hablantes casi nativos que quieren cerrar la brecha final. Perfecto para profesionales que publican en inglés, académicos que escriben a nivel internacional, o cualquiera que se niegue a conformarse con 'muy bueno' cuando 'excelente' está a su alcance.",
        "c2_learn_title": "Qué aprenderás",
        "c2_learn_items": [
            "Entender prácticamente todo — hablado o escrito, con cualquier acento",
            "Resumir y sintetizar información compleja de múltiples fuentes",
            "Escribir con elegancia, sutileza y control estilístico",
            "Usar el humor, la ironía y las referencias culturales como un nativo",
            "Alcanzar una fluidez total sin lagunas observables",
        ],
        "c2_format_title": "Formato y horario",
        "c2_format_desc": "Totalmente flexible y altamente personalizado. Solo individual.",
        "c2_price_title": "Precio",
        "c2_price_desc": "Desde $200 USD / mes individual. Programa personalizado adaptado a tus objetivos específicos.",
        "c2_cta": "Inscribirse en C2 →",
        "c2_back": "← Volver a todos los cursos",

        # About
        "about_title": "Quiénes somos",
        "about_meet_title": "Conocé a Flor",
        "about_meet_body": "¡Hola! Soy Flor, profesora de inglés con título, radicada en Argentina. Llevo más de 10 años ayudando a estudiantes de todas las edades y niveles a mejorar su inglés. Ya sea que te estés preparando para un examen, necesites inglés para el trabajo, o simplemente quieras sentirte más seguro al hablar — estoy acá para ayudarte.",
        "about_approach_title": "Mi método",
        "about_approach_body": "Creo que la mejor manera de aprender un idioma es usándolo. Mis clases se centran en la conversación real, vocabulario práctico y construir confianza desde el primer día. Cada estudiante es diferente, por eso adapto cada clase a tus objetivos, tu nivel y tu ritmo.",
        "about_why_title": "¿Por qué elegir English with Flor?",
        "about_why_1": "Clases personalizadas según tus objetivos y nivel",
        "about_why_2": "Horarios flexibles — las clases se adaptan a tu vida",
        "about_why_3": "Un ambiente relajado y de apoyo donde los errores son bienvenidos",
        "about_why_4": "Experiencia con estudiantes de Argentina y de todo el mundo",
        "about_cta": "Contactanos",

        # Contact
        "contact_title": "Contáctanos",
        "contact_email": "Correo electrónico",
        "contact_phone": "Teléfono",
        "contact_name_label": "Tu nombre",
        "contact_email_label": "Tu correo electrónico",
        "contact_message_label": "Tu mensaje",
        "contact_submit": "Enviar mensaje",
        "contact_success": "¡Gracias por tu mensaje! Te responderemos pronto.",
        "contact_whatsapp_btn": "O chatea con Flor por WhatsApp →",
        "contact_whatsapp_url": "https://wa.me/0000000000?text=Hola%20Flor%2C%20te%20envié%20un%20mensaje%20por%20la%20web",
        "error_message_length": "El mensaje debe tener entre 10 y 2000 caracteres.",

        # Register — page text
        "register_title": "Crear una cuenta",
        "already_have_account": "¿Ya tienes una cuenta?",
        "login_link": "Inicia sesión aquí",

        # Register — field labels
        "register_first_name": "Nombre",
        "register_last_name": "Apellido",
        "register_email": "Correo electrónico",
        "register_username": "Nombre de usuario",
        "register_password": "Contraseña",
        "register_confirm": "Confirmar contraseña",
        "register_submit": "Registrarse",

        # Register — validator error messages (keys match message= strings in forms.py)
        "error_field_required": "Este campo es obligatorio.",
        "error_name_length": "Debe tener al menos 2 caracteres.",
        "error_username_length": "Debe tener entre 3 y 80 caracteres.",
        "error_invalid_email": "Por favor introduce un correo electrónico válido.",
        "error_password_too_short": "La contraseña debe tener al menos 8 caracteres.",
        "error_passwords_must_match": "Las contraseñas deben coincidir.",

        # Login
        "login_title": "Iniciar sesión",
        "no_account": "¿No tienes una cuenta?",
        "register_link": "Regístrate aquí",
        "logout": "Cerrar sesión",

        # Enrolment
        "enrol_title": "Inscribirse en un curso",

        # Enrolment form — address fields
        "enrol_address_title":   "Tu dirección",
        "enrol_address_line":    "Dirección",
        "enrol_city":            "Ciudad",
        "enrol_province":        "Provincia / Estado",
        "enrol_country":         "País",
        "enrol_postcode":        "Código postal",

        # Word of the day
        "wotd_label": "Palabra del día",
        "wotd_no_equiv": "Sin equivalente directo en español",


        # Dashboard
        "dashboard_title": "Bienvenido",
        "dashboard_your_details": "Tus datos",
        "dashboard_username": "Usuario",
        "dashboard_email": "Correo electrónico",
        "dashboard_enrolment": "Tu inscripción",
        "dashboard_course": "Curso",
        "dashboard_passport": "Número de pasaporte",
        "dashboard_not_enrolled": "Aún no estás inscrito en ningún curso.",
        "dashboard_enrol_link": "Inscríbete ahora",

        # Dashboard — edit profile
        "edit_profile_title": "Editar tus datos",
        "edit_profile_first_name": "Nombre",
        "edit_profile_last_name": "Apellido",
        "edit_profile_email": "Correo electrónico",
        "edit_profile_submit": "Guardar cambios",
        "edit_profile_success": "Tus datos han sido actualizados.",
        "edit_profile_btn": "Editar datos",
        "edit_profile_cancel": "Cancelar",

        # Dashboard — edit address
        "edit_address_title":   "Editar tu dirección",
        "edit_address_submit":  "Guardar cambios",
        "edit_address_success": "Tu dirección ha sido actualizada.",
        "edit_address_btn":     "Editar dirección",
        "edit_address_cancel":  "Cancelar",

        # Dashboard — change password
        "change_pw_title": "Cambiar tu contraseña",
        "change_pw_current": "Contraseña actual",
        "change_pw_new": "Nueva contraseña",
        "change_pw_confirm": "Confirmar nueva contraseña",
        "change_pw_submit": "Cambiar contraseña",
        "change_pw_success": "Tu contraseña ha sido cambiada.",
        "change_pw_btn": "Cambiar contraseña",
        "change_pw_cancel": "Cancelar",
        "error_wrong_password": "La contraseña actual es incorrecta.",

        # Dashboard — delete account
        "delete_account_title": "Eliminar tu cuenta",
        "delete_account_warning": "Esta acción es permanente. Tu cuenta, datos personales e inscripción serán eliminados de inmediato. No se puede deshacer.",
        "delete_account_password": "Introduce tu contraseña para confirmar",
        "delete_account_submit": "Eliminar mi cuenta",
        "delete_account_success": "Tu cuenta ha sido eliminada.",
        "delete_account_btn": "Eliminar cuenta",
        "delete_account_cancel": "Cancelar",

        # Errors
        "error_username_taken": "Ese nombre de usuario ya está en uso. Por favor elige otro.",
        "error_email_taken": "Ya existe una cuenta con ese correo electrónico.",
        "error_invalid_credentials": "Usuario o contraseña incorrectos. Por favor inténtalo de nuevo.",
        "error_argentina_fields": "Por favor introduce tu CUIT/CUIL y DNI.",
        "error_passport_required": "Por favor introduce tu número de pasaporte.",
        "error_address_length":  "La dirección no puede superar los 200 caracteres.",
        "error_city_length":     "La ciudad no puede superar los 100 caracteres.",
        "error_province_length": "La provincia / estado no puede superar los 100 caracteres.",
        "error_country_length":  "El país no puede superar los 100 caracteres.",
        "error_postcode_length": "El código postal no puede superar los 20 caracteres.",

        # Error pages
        "error_404_title": "Página no encontrada",
        "error_404_message": "Lo sentimos, la página que buscas no existe o ha sido movida.",
        "error_500_title": "Algo salió mal",
        "error_500_message": "Estamos teniendo dificultades técnicas. Por favor inténtalo más tarde.",
        "error_go_home": "Ir a la página de inicio",
    }
}
