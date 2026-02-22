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
        "lang_toggle": "Español",

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

        # Home — testimonial
        "testimonial_quote": "In six months with Flor, I went from barely ordering coffee to presenting quarterly results to our London office — in English.",
        "testimonial_author": "María Fernández",
        "testimonial_location": "Buenos Aires · B2 Graduate",

        # Home — CTA
        "cta_title": "Book your level test",
        "cta_desc": "Not sure where to start? Take a level test with Flor and find out exactly where you are — and where you could go.",
        "cta_btn": "Book your test now →",

        # Footer
        "footer_copy": "© 2026 English with Flor. All rights reserved.",

        # Courses — listing page
        "courses_title": "Our Courses",
        "course_name": "English for All Levels",
        "course_desc": "Whether you are a complete beginner or looking to polish your fluency, our English course is tailored to you. Classes are available one-to-one or in small groups.",

        "courses_intro": "Choose the level that fits where you are today. Every course is taught in small groups or one-to-one, so you get real attention — not just a seat in a class.",
        "courses_view_btn": "View course →",

        # Beginner course
        "beg_title": "Beginner English",
        "beg_level": "A1 – A2",
        "beg_tagline": "Start from zero and build real, usable English from day one.",
        "beg_who_title": "Who is this for?",
        "beg_who_desc": "Perfect for complete beginners or anyone who studied English years ago and needs a confident restart. No prior knowledge needed — just curiosity and a willingness to speak.",
        "beg_learn_title": "What you will learn",
        "beg_learn_items": [
            "Introduce yourself and talk about your daily life",
            "Ask and answer questions in everyday situations",
            "Understand simple spoken and written English",
            "Build a foundation of 1,000+ high-frequency words",
            "Gain confidence to speak without freezing",
        ],
        "beg_format_title": "Format & schedule",
        "beg_format_desc": "Two 60-minute live sessions per week, available mornings or evenings. Choose one-to-one with Flor or a small group of up to 4 students.",
        "beg_price_title": "Pricing",
        "beg_price_desc": "From $80 USD / month for group classes · $150 USD / month one-to-one. Includes all materials and a monthly progress review.",
        "beg_cta": "Enrol in Beginner →",
        "beg_back": "← Back to all courses",

        # Intermediate course
        "int_title": "Intermediate English",
        "int_level": "B1 – B2",
        "int_tagline": "Break through the plateau and start speaking with real fluency.",
        "int_who_title": "Who is this for?",
        "int_who_desc": "For students who already know the basics but feel stuck — you understand a lot but struggle to express yourself quickly and naturally. This course is where fluency begins.",
        "int_learn_title": "What you will learn",
        "int_learn_items": [
            "Discuss opinions, news, and complex topics in English",
            "Write clear emails, messages, and short essays",
            "Understand native speakers at natural speed",
            "Expand vocabulary into professional and social contexts",
            "Correct your most common grammar mistakes for good",
        ],
        "int_format_title": "Format & schedule",
        "int_format_desc": "Two 75-minute live sessions per week. Focus shifts toward conversation and debate. One-to-one or small group available.",
        "int_price_title": "Pricing",
        "int_price_desc": "From $90 USD / month for group classes · $165 USD / month one-to-one. Includes all materials and a monthly progress review.",
        "int_cta": "Enrol in Intermediate →",
        "int_back": "← Back to all courses",

        # Advanced course
        "adv_title": "Advanced English",
        "adv_level": "C1 – C2",
        "adv_tagline": "Reach native-level precision in professional and academic English.",
        "adv_who_title": "Who is this for?",
        "adv_who_desc": "For high-level speakers who want to polish their English for work presentations, international business, academic writing, or simply to sound as confident in English as they do in Spanish.",
        "adv_learn_title": "What you will learn",
        "adv_learn_items": [
            "Speak with precision, nuance, and native-level vocabulary",
            "Present and negotiate confidently in professional settings",
            "Write at an academic or business standard",
            "Understand accents, humour, and cultural subtleties",
            "Eliminate fossilised errors and refine your personal style",
        ],
        "adv_format_title": "Format & schedule",
        "adv_format_desc": "Flexible scheduling — one or two sessions per week, tailored to your professional goals. One-to-one only at this level for maximum personalisation.",
        "adv_price_title": "Pricing",
        "adv_price_desc": "From $180 USD / month one-to-one. Fully tailored curriculum — no fixed materials cost.",
        "adv_cta": "Enrol in Advanced →",
        "adv_back": "← Back to all courses",

        # About
        "about_title": "About Us",
        "about_body": "English with Flor has been helping students reach their language goals since 2010. Our qualified teachers make learning fun, practical, and effective.",

        # Contact
        "contact_title": "Contact Us",
        "contact_email": "Email",
        "contact_phone": "Phone",

        # Register
        "register_title": "Create an Account",
        "already_have_account": "Already have an account?",
        "login_link": "Log in here",

        # Login
        "login_title": "Log In",
        "no_account": "Don't have an account?",
        "register_link": "Register here",
        "logout": "Log Out",

        # Enrolment
        "enrol_title": "Enrol on a Course",

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

        # Errors
        "error_username_taken": "That username is already taken. Please choose another.",
        "error_email_taken": "An account with that email already exists.",
        "error_invalid_credentials": "Invalid username or password. Please try again.",
        "error_argentina_fields": "Please enter both your CUIT/CUIL and DNI.",
        "error_passport_required": "Please enter your passport number.",
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
        "lang_toggle": "English",

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

        # Home — testimonial
        "testimonial_quote": "En seis meses con Flor, pasé de apenas pedir un café a presentar resultados trimestrales en nuestra oficina de Londres — en inglés.",
        "testimonial_author": "María Fernández",
        "testimonial_location": "Buenos Aires · Graduada B2",

        # Home — CTA
        "cta_title": "Reserva tu test de nivel",
        "cta_desc": "¿No sabes por dónde empezar? Haz un test de nivel con Flor y descubre exactamente dónde estás — y hasta dónde puedes llegar.",
        "cta_btn": "Reserva tu test ahora →",

        # Footer
        "footer_copy": "© 2026 English with Flor. Todos los derechos reservados.",

        # Courses — listing page
        "courses_title": "Nuestros cursos",
        "course_name": "Inglés para todos los niveles",
        "course_desc": "Tanto si eres principiante como si quieres perfeccionar tu fluidez, nuestro curso de inglés se adapta a ti. Las clases están disponibles de forma individual o en grupos pequeños.",

        "courses_intro": "Elige el nivel que se adapta a dónde estás hoy. Cada curso se imparte en grupos pequeños o de forma individual, para que recibas atención real.",
        "courses_view_btn": "Ver curso →",

        # Beginner course
        "beg_title": "Inglés para principiantes",
        "beg_level": "A1 – A2",
        "beg_tagline": "Empieza desde cero y construye un inglés real y útil desde el primer día.",
        "beg_who_title": "¿Para quién es este curso?",
        "beg_who_desc": "Perfecto para principiantes absolutos o para quienes estudiaron inglés hace años y necesitan un reinicio con confianza. No se necesitan conocimientos previos — solo curiosidad y ganas de hablar.",
        "beg_learn_title": "Qué aprenderás",
        "beg_learn_items": [
            "Presentarte y hablar sobre tu vida cotidiana",
            "Hacer y responder preguntas en situaciones del día a día",
            "Entender inglés oral y escrito sencillo",
            "Construir una base de más de 1.000 palabras de alta frecuencia",
            "Ganar confianza para hablar sin bloquearte",
        ],
        "beg_format_title": "Formato y horario",
        "beg_format_desc": "Dos sesiones en vivo de 60 minutos por semana, disponibles por las mañanas o por las tardes. Elige clases individuales con Flor o un grupo de hasta 4 estudiantes.",
        "beg_price_title": "Precio",
        "beg_price_desc": "Desde $80 USD / mes en grupo · $150 USD / mes individual. Incluye todos los materiales y una revisión mensual de progreso.",
        "beg_cta": "Inscribirse en Principiantes →",
        "beg_back": "← Volver a todos los cursos",

        # Intermediate course
        "int_title": "Inglés intermedio",
        "int_level": "B1 – B2",
        "int_tagline": "Supera el estancamiento y empieza a hablar con fluidez real.",
        "int_who_title": "¿Para quién es este curso?",
        "int_who_desc": "Para estudiantes que ya conocen lo básico pero se sienten bloqueados — entienden mucho pero les cuesta expresarse con rapidez y naturalidad. Aquí empieza la fluidez.",
        "int_learn_title": "Qué aprenderás",
        "int_learn_items": [
            "Hablar sobre opiniones, noticias y temas complejos en inglés",
            "Escribir correos, mensajes y textos cortos con claridad",
            "Entender a hablantes nativos a velocidad natural",
            "Ampliar el vocabulario en contextos profesionales y sociales",
            "Corregir tus errores gramaticales más frecuentes de una vez por todas",
        ],
        "int_format_title": "Formato y horario",
        "int_format_desc": "Dos sesiones en vivo de 75 minutos por semana. El enfoque se centra en la conversación y el debate. Disponible de forma individual o en grupo pequeño.",
        "int_price_title": "Precio",
        "int_price_desc": "Desde $90 USD / mes en grupo · $165 USD / mes individual. Incluye todos los materiales y una revisión mensual de progreso.",
        "int_cta": "Inscribirse en Intermedio →",
        "int_back": "← Volver a todos los cursos",

        # Advanced course
        "adv_title": "Inglés avanzado",
        "adv_level": "C1 – C2",
        "adv_tagline": "Alcanza la precisión de un hablante nativo en inglés profesional y académico.",
        "adv_who_title": "¿Para quién es este curso?",
        "adv_who_desc": "Para hablantes de nivel alto que quieren perfeccionar su inglés para presentaciones laborales, negocios internacionales, escritura académica, o simplemente sonar tan seguros en inglés como en español.",
        "adv_learn_title": "Qué aprenderás",
        "adv_learn_items": [
            "Hablar con precisión, matiz y vocabulario de nivel nativo",
            "Presentar y negociar con confianza en entornos profesionales",
            "Escribir con un estándar académico o empresarial",
            "Entender acentos, humor y subtilezas culturales",
            "Eliminar errores arraigados y pulir tu estilo personal",
        ],
        "adv_format_title": "Formato y horario",
        "adv_format_desc": "Horario flexible — una o dos sesiones por semana, adaptadas a tus objetivos profesionales. Solo individual a este nivel para máxima personalización.",
        "adv_price_title": "Precio",
        "adv_price_desc": "Desde $180 USD / mes individual. Programa completamente personalizado — sin coste fijo de materiales.",
        "adv_cta": "Inscribirse en Avanzado →",
        "adv_back": "← Volver a todos los cursos",

        # About
        "about_title": "Quiénes somos",
        "about_body": "English with Flor lleva desde 2010 ayudando a los estudiantes a alcanzar sus metas lingüísticas. Nuestros profesores cualificados hacen que aprender sea divertido, práctico y eficaz.",

        # Contact
        "contact_title": "Contáctanos",
        "contact_email": "Correo electrónico",
        "contact_phone": "Teléfono",

        # Register
        "register_title": "Crear una cuenta",
        "already_have_account": "¿Ya tienes una cuenta?",
        "login_link": "Inicia sesión aquí",

        # Login
        "login_title": "Iniciar sesión",
        "no_account": "¿No tienes una cuenta?",
        "register_link": "Regístrate aquí",
        "logout": "Cerrar sesión",

        # Enrolment
        "enrol_title": "Inscribirse en un curso",

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

        # Errors
        "error_username_taken": "Ese nombre de usuario ya está en uso. Por favor elige otro.",
        "error_email_taken": "Ya existe una cuenta con ese correo electrónico.",
        "error_invalid_credentials": "Usuario o contraseña incorrectos. Por favor inténtalo de nuevo.",
        "error_argentina_fields": "Por favor introduce tu CUIT/CUIL y DNI.",
        "error_passport_required": "Por favor introduce tu número de pasaporte.",
    }
}
