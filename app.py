import os
import json

from flask import Flask, render_template_string
from dotenv import load_dotenv

load_dotenv(override=True)

app = Flask(__name__)


def get_list(name):
    """
    .env dan JSON array olish.
    Xato bo'lsa saytni buzmaydi.
    """
    value = os.getenv(name, "").strip()

    if not value:
        return []

    try:
        result = json.loads(value)

        if isinstance(result, list):
            return result

    except Exception as e:
        print(f"[ENV ERROR] {name}: {e}")

    return []


DATA = {
    "name": os.getenv("SALON_NAME", "Гранд Элит"),
    "tagline": os.getenv("SALON_TAGLINE", "Beauty & Barber"),
    "description": os.getenv(
        "SALON_DESCRIPTION",
        "Салон красоты и барбершоп в Самарканде."
    ),

    "address": os.getenv(
        "SALON_ADDRESS",
        "ул. Мир Саид Барака, 11/13"
    ),

    "phone": os.getenv(
        "SALON_PHONE",
        "+998 93 333 99 97"
    ),

    "rating": os.getenv("SALON_RATING", "4.8"),

    "reviews_count": os.getenv(
        "SALON_REVIEWS_COUNT",
        "90"
    ),

    "hours": os.getenv(
        "SALON_HOURS",
        "Открыто до 20:00"
    ),

    "maps_url": os.getenv(
        "SALON_MAPS_URL",
        "https://yandex.uz/maps/org/grand_elite/24013429655/"
    ),

    "services": get_list("SERVICES"),
    "prices": get_list("PRICES"),
    "reviews": get_list("REVIEWS"),
    "features": get_list("FEATURES"),
    "about_points": get_list("ABOUT_POINTS"),

    "about_title": os.getenv(
        "ABOUT_TITLE",
        "Красота в деталях."
    ),

    "about_text": os.getenv(
        "ABOUT_TEXT",
        "Гранд Элит — пространство красоты в Самарканде."
    )
}


print()
print("=" * 55)
print(" GRAND ELITE WEB APP")
print("=" * 55)
print(f"Salon:       {DATA['name']}")
print(f"Services:    {len(DATA['services'])}")
print(f"Prices:      {len(DATA['prices'])}")
print(f"Reviews:     {len(DATA['reviews'])}")
print(f"Features:    {len(DATA['features'])}")
print(f"About:       {len(DATA['about_points'])}")
print("=" * 55)
print()


HTML = r"""
<!DOCTYPE html>

<html lang="ru">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>{{ data.name }} — {{ data.tagline }}</title>

<link rel="preconnect" href="https://fonts.googleapis.com">

<link
    rel="preconnect"
    href="https://fonts.gstatic.com"
    crossorigin
>

<link
    href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap"
    rel="stylesheet"
>


<style>

/* =========================================================
   BASE
========================================================= */

:root {

    --bg: #f5f4f1;
    --white: #ffffff;
    --black: #171717;
    --gray: #77736d;
    --light: #e9e7e2;
    --line: rgba(0,0,0,.08);

    --radius: 28px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {

    font-family: "Manrope", sans-serif;

    background: var(--bg);

    color: var(--black);

    overflow-x: hidden;
}

a {
    color: inherit;
    text-decoration: none;
}

button {
    font-family: inherit;
}

.container {

    width: min(
        1160px,
        calc(100% - 40px)
    );

    margin: auto;
}


/* =========================================================
   NAV
========================================================= */

nav {

    position: fixed;

    top: 0;
    left: 0;

    width: 100%;

    z-index: 1000;

    padding: 18px 0;

    transition:
        background .3s ease,
        backdrop-filter .3s ease,
        border .3s ease;
}

nav.scrolled {

    background: rgba(245,244,241,.86);

    backdrop-filter: blur(18px);

    border-bottom: 1px solid var(--line);
}

.nav-inner {

    display: flex;

    align-items: center;

    justify-content: space-between;
}

.logo {

    font-size: 20px;

    font-weight: 800;

    letter-spacing: -1px;
}

.nav-links {

    display: flex;

    gap: 28px;

    color: #66625c;

    font-size: 13px;
}

.nav-links a {

    transition: color .25s ease;
}

.nav-links a:hover {
    color: #000;
}

.nav-button {

    padding: 12px 20px;

    background: var(--black);

    color: white;

    border-radius: 100px;

    font-size: 13px;

    font-weight: 700;

    transition:
        transform .25s ease,
        opacity .25s ease;
}

.nav-button:hover {

    transform: translateY(-2px);

    opacity: .88;
}


/* =========================================================
   HERO
========================================================= */

.hero {

    min-height: 100vh;

    display: flex;

    align-items: center;

    padding: 130px 0 80px;
}

.hero-grid {

    display: grid;

    grid-template-columns:
        1.2fr .8fr;

    gap: 70px;

    align-items: center;
}

.eyebrow {

    display: flex;

    align-items: center;

    gap: 8px;

    margin-bottom: 25px;

    color: var(--gray);

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 1.5px;

    text-transform: uppercase;
}

.dot {

    width: 7px;
    height: 7px;

    border-radius: 50%;

    background: #222;
}

h1 {

    font-size:
        clamp(58px, 8vw, 105px);

    line-height: .88;

    letter-spacing: -6px;

    font-weight: 800;
}

.hero-description {

    max-width: 560px;

    margin-top: 30px;

    color: var(--gray);

    font-size: 15px;

    line-height: 1.8;
}

.hero-actions {

    display: flex;

    flex-wrap: wrap;

    gap: 12px;

    margin-top: 35px;
}

.btn {

    display: inline-flex;

    align-items: center;

    justify-content: center;

    padding: 15px 23px;

    border-radius: 100px;

    font-size: 13px;

    font-weight: 700;

    transition:
        transform .3s ease,
        box-shadow .3s ease,
        background .3s ease;
}

.btn-dark {

    background: var(--black);

    color: white;
}

.btn-light {

    border: 1px solid var(--line);

    background: transparent;
}

.btn:hover {

    transform: translateY(-3px);

    box-shadow:
        0 12px 30px rgba(0,0,0,.08);
}


/* =========================================================
   HERO CARD
========================================================= */

.hero-card {

    position: relative;

    min-height: 450px;

    padding: 38px;

    overflow: hidden;

    border-radius: 42px;

    background: var(--light);

    display: flex;

    flex-direction: column;

    justify-content: space-between;
}

.hero-card::before {

    content: "";

    position: absolute;

    width: 320px;
    height: 320px;

    top: -100px;
    right: -100px;

    border-radius: 50%;

    background: #d8d5cf;
}

.hero-card::after {

    content: "";

    position: absolute;

    width: 220px;
    height: 220px;

    bottom: -100px;
    left: -100px;

    border-radius: 50%;

    background: #faf9f6;
}

.rating {

    position: relative;

    z-index: 2;

    display: flex;

    justify-content: space-between;
}

.rating-number {

    font-size: 65px;

    line-height: 1;

    font-weight: 800;

    letter-spacing: -5px;
}

.stars {

    margin-top: 8px;

    letter-spacing: 4px;
}

.rating-count {

    color: var(--gray);

    font-size: 12px;
}

.hero-bottom {

    position: relative;

    z-index: 2;
}

.hero-bottom strong {

    font-size: 17px;
}

.hero-bottom p {

    margin-top: 8px;

    color: var(--gray);

    font-size: 13px;

    line-height: 1.6;
}


/* =========================================================
   SECTIONS
========================================================= */

section {
    padding: 110px 0;
}

.section-header {

    display: flex;

    align-items: flex-end;

    justify-content: space-between;

    gap: 30px;

    margin-bottom: 45px;
}

.section-number {

    margin-bottom: 12px;

    color: #aaa;

    font-size: 12px;

    font-weight: 600;
}

.section-title {

    font-size:
        clamp(42px, 5vw, 68px);

    line-height: .95;

    letter-spacing: -4px;
}

.section-text {

    max-width: 410px;

    color: var(--gray);

    font-size: 14px;

    line-height: 1.8;
}


/* =========================================================
   SERVICES
========================================================= */

.services {

    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 14px;
}

.service {

    min-height: 210px;

    padding: 30px;

    background: var(--white);

    border: 1px solid var(--line);

    border-radius: var(--radius);

    transition:
        transform .4s cubic-bezier(.2,.8,.2,1),
        box-shadow .4s ease;
}

.service:hover {

    transform: translateY(-8px);

    box-shadow:
        0 25px 50px rgba(0,0,0,.07);
}

.service-number {

    color: #aaa;

    font-size: 12px;
}

.service-icon {

    width: 42px;
    height: 42px;

    margin-top: 25px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    background: var(--bg);

    font-size: 17px;
}

.service h3 {

    margin-top: 18px;

    font-size: 19px;
}

.service p {

    margin-top: 8px;

    color: var(--gray);

    font-size: 12px;

    line-height: 1.6;
}


/* =========================================================
   PRICES
========================================================= */

.price-wrapper {

    padding: 45px;

    background: var(--black);

    color: white;

    border-radius: 34px;
}

.price-row {

    display: grid;

    grid-template-columns:
        1fr auto;

    align-items: center;

    padding: 21px 0;

    border-bottom:
        1px solid rgba(255,255,255,.12);
}

.price-row:last-child {
    border-bottom: none;
}

.price-name {

    font-weight: 600;
}

.price-value {

    color: #d2d0cc;

    font-size: 14px;

    font-weight: 700;
}


/* =========================================================
   ABOUT
========================================================= */

.about {

    display: grid;

    grid-template-columns:
        1fr 1fr;

    gap: 70px;

    align-items: center;
}

.about-big {

    font-size:
        clamp(42px, 6vw, 76px);

    line-height: .94;

    letter-spacing: -4px;

    font-weight: 800;
}

.about-text {

    margin-top: 25px;

    color: var(--gray);

    font-size: 14px;

    line-height: 1.9;
}

.about-points {

    display: grid;

    gap: 12px;
}

.about-point {

    display: flex;

    align-items: center;

    gap: 13px;

    padding: 20px 22px;

    background: white;

    border: 1px solid var(--line);

    border-radius: 18px;

    font-size: 13px;

    font-weight: 600;

    transition:
        transform .3s ease;
}

.about-point:hover {

    transform: translateX(7px);
}

.check {

    width: 25px;
    height: 25px;

    flex: 0 0 25px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    background: var(--black);

    color: white;

    font-size: 11px;
}


/* =========================================================
   REVIEWS
========================================================= */

.reviews {

    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 14px;
}

.review {

    padding: 28px;

    background: white;

    border: 1px solid var(--line);

    border-radius: var(--radius);

    transition:
        transform .35s ease,
        box-shadow .35s ease;
}

.review:hover {

    transform: translateY(-7px);

    box-shadow:
        0 20px 40px rgba(0,0,0,.06);
}

.review-top {

    display: flex;

    justify-content: space-between;

    gap: 15px;
}

.review-name {

    font-size: 14px;

    font-weight: 800;
}

.review-date {

    color: #999;

    font-size: 10px;
}

.review-stars {

    margin-top: 17px;

    font-size: 12px;

    letter-spacing: 3px;
}

.review-text {

    margin-top: 17px;

    color: #68645e;

    font-size: 12px;

    line-height: 1.8;
}


/* =========================================================
   CONTACT
========================================================= */

.contact-box {

    display: grid;

    grid-template-columns:
        1fr 1fr;

    gap: 70px;

    padding: 60px;

    background: var(--light);

    border-radius: 40px;
}

.contact-title {

    font-size:
        clamp(43px, 6vw, 75px);

    line-height: .92;

    letter-spacing: -4px;
}

.contact-items {

    display: grid;

    gap: 24px;
}

.contact-item span {

    display: block;

    margin-bottom: 6px;

    color: #888;

    font-size: 10px;

    letter-spacing: 1px;

    text-transform: uppercase;
}

.contact-item strong {

    font-size: 17px;
}


/* =========================================================
   FOOTER
========================================================= */

footer {
    padding: 45px 0;
}

.footer-inner {

    display: flex;

    justify-content: space-between;

    padding-top: 25px;

    border-top: 1px solid var(--line);

    color: #888;

    font-size: 12px;
}


/* =========================================================
   ANIMATION
========================================================= */

/*
    MUHIM:

    Oldin opacity:0 berilgani sababli JS ishlamasa
    saytning hamma ma'lumotlari yo'qolib qolardi.

    Endi default holatda elementlar KO'RINADI.
*/

.reveal {

    opacity: 1;

    transform: translateY(0);
}


/*
    JavaScript ishlayotganida
    faqat .js-enabled mavjud bo'lsa animatsiya yoqiladi.
*/

.js-enabled .reveal {

    opacity: 0;

    transform: translateY(28px);

    transition:
        opacity .75s ease,
        transform .75s cubic-bezier(.2,.8,.2,1);
}

.js-enabled .reveal.visible {

    opacity: 1;

    transform: translateY(0);
}


/* =========================================================
   MOBILE
========================================================= */

@media(max-width: 850px) {

    .nav-links {
        display: none;
    }

    .hero-grid {

        grid-template-columns: 1fr;
    }

    .services,
    .reviews {

        grid-template-columns:
            repeat(2, 1fr);
    }

    .about {

        grid-template-columns: 1fr;
    }

    .contact-box {

        grid-template-columns: 1fr;
    }
}


@media(max-width: 560px) {

    .container {

        width:
            calc(100% - 28px);
    }

    section {

        padding: 75px 0;
    }

    .hero {

        padding-top: 110px;
    }

    h1 {

        font-size: 58px;

        letter-spacing: -4px;
    }

    .hero-card {

        min-height: 340px;
    }

    .services,
    .reviews {

        grid-template-columns: 1fr;
    }

    .section-header {

        display: block;
    }

    .section-text {

        margin-top: 18px;
    }

    .price-wrapper {

        padding: 28px;
    }

    .contact-box {

        padding: 32px;

        border-radius: 28px;
    }

    .footer-inner {

        display: block;
    }

    .footer-inner div:last-child {

        margin-top: 10px;
    }
}

</style>

</head>


<body>


<nav id="nav">

<div class="container nav-inner">

<a class="logo" href="#top">
{{ data.name }}
</a>

<div class="nav-links">

<a href="#services">Услуги</a>

<a href="#prices">Цены</a>

<a href="#about">О салоне</a>

<a href="#reviews">Отзывы</a>

<a href="#contact">Контакты</a>

</div>

<a
    class="nav-button"
    href="tel:{{ data.phone }}"
>
Записаться
</a>

</div>

</nav>


<main id="top">


<!-- HERO -->

<section class="hero">

<div class="container hero-grid">


<div class="reveal">

<div class="eyebrow">

<span class="dot"></span>

Самарканд · Beauty & Barber

</div>


<h1>
{{ data.name }}
</h1>


<p class="hero-description">
{{ data.description }}
</p>


<div class="hero-actions">

<a
    class="btn btn-dark"
    href="tel:{{ data.phone }}"
>
Записаться
</a>

<a
    class="btn btn-light"
    href="{{ data.maps_url }}"
    target="_blank"
>
Открыть карту
</a>

</div>

</div>


<div class="hero-card reveal">

<div class="rating">

<div>

<div class="rating-number">
{{ data.rating }}
</div>

<div class="stars">
★★★★★
</div>

</div>

<div class="rating-count">
{{ data.reviews_count }} оценок
</div>

</div>


<div class="hero-bottom">

<strong>
{{ data.hours }}
</strong>

<p>
{{ data.address }}
</p>

</div>

</div>

</div>

</section>


<!-- SERVICES -->

<section id="services">

<div class="container">


<div class="section-header reveal">

<div>

<div class="section-number">
01 / УСЛУГИ
</div>

<h2 class="section-title">
Для вашего образа.
</h2>

</div>


<p class="section-text">
Профессиональные услуги красоты и ухода
в одном пространстве.
</p>

</div>


<div class="services">

{% if data.services %}

{% for service in data.services %}

<div class="service reveal">

<div class="service-number">
{{ "%02d"|format(loop.index) }}
</div>

<div class="service-icon">
✦
</div>

<h3>
{{ service.name }}
</h3>

<p>
{{ service.description }}
</p>

</div>

{% endfor %}

{% else %}

<div class="service reveal">

<h3>
Услуги
</h3>

<p>
Информация об услугах будет добавлена.
</p>

</div>

{% endif %}

</div>

</div>

</section>


<!-- PRICES -->

<section id="prices">

<div class="container">


<div class="section-header reveal">

<div>

<div class="section-number">
02 / ЦЕНЫ
</div>

<h2 class="section-title">
Стоимость.
</h2>

</div>

<p class="section-text">
Стоимость популярных услуг салона.
</p>

</div>


<div class="price-wrapper reveal">

{% if data.prices %}

{% for price in data.prices %}

<div class="price-row">

<div class="price-name">
{{ price.name }}
</div>

<div class="price-value">
{{ price.price }}
</div>

</div>

{% endfor %}

{% else %}

<div class="price-row">

<div class="price-name">
Стоимость
</div>

<div class="price-value">
Уточняйте по телефону
</div>

</div>

{% endif %}

</div>

</div>

</section>


<!-- ABOUT -->

<section id="about">

<div class="container">


<div class="section-header reveal">

<div>

<div class="section-number">
03 / О САЛОНЕ
</div>

<h2 class="section-title">
{{ data.about_title }}
</h2>

</div>

</div>


<div class="about">


<div class="reveal">

<div class="about-big">
{{ data.about_title }}
</div>

<p class="about-text">
{{ data.about_text }}
</p>

</div>


<div class="about-points">

{% if data.about_points %}

{% for point in data.about_points %}

<div class="about-point reveal">

<div class="check">
✓
</div>

{{ point }}

</div>

{% endfor %}

{% else %}

<div class="about-point reveal">

<div class="check">
✓
</div>

Профессиональные мастера

</div>

{% endif %}

</div>

</div>

</div>

</section>


<!-- REVIEWS -->

<section id="reviews">

<div class="container">


<div class="section-header reveal">

<div>

<div class="section-number">
04 / ОТЗЫВЫ
</div>

<h2 class="section-title">
Что говорят гости.
</h2>

</div>


<p class="section-text">

{{ data.rating }} из 5 на основе
{{ data.reviews_count }} оценок.

</p>

</div>


<div class="reviews">

{% if data.reviews %}

{% for review in data.reviews %}

<article class="review reveal">

<div class="review-top">

<div class="review-name">
{{ review.name }}
</div>

<div class="review-date">
{{ review.date }}
</div>

</div>

<div class="review-stars">
★★★★★
</div>

<p class="review-text">
{{ review.text }}
</p>

</article>

{% endfor %}

{% else %}

<article class="review reveal">

<div class="review-name">
Отзывы
</div>

<p class="review-text">
Отзывы клиентов скоро появятся.
</p>

</article>

{% endif %}

</div>

</div>

</section>


<!-- CONTACT -->

<section id="contact">

<div class="container">


<div class="contact-box reveal">


<div>

<div class="eyebrow">

<span class="dot"></span>

Контакты

</div>


<h2 class="contact-title">
Будем рады
видеть вас.
</h2>

</div>


<div class="contact-items">


<div class="contact-item">

<span>
Адрес
</span>

<strong>
{{ data.address }}
</strong>

</div>


<div class="contact-item">

<span>
Телефон
</span>

<strong>

<a href="tel:{{ data.phone }}">
{{ data.phone }}
</a>

</strong>

</div>


<div class="contact-item">

<span>
Время работы
</span>

<strong>
{{ data.hours }}
</strong>

</div>


<div>

<a
    class="btn btn-dark"
    href="{{ data.maps_url }}"
    target="_blank"
>
Построить маршрут
</a>

</div>


</div>

</div>

</div>

</section>


</main>


<footer>

<div class="container footer-inner">

<div>
© 2026 {{ data.name }}
</div>

<div>
Самарканд · Uzbekistan
</div>

</div>

</footer>


<script>

/*
    JS ishlayotganini belgilaymiz.
*/

document.documentElement.classList.add("js-enabled");


/*
    NAV
*/

const nav = document.getElementById("nav");

window.addEventListener("scroll", function () {

    if (window.scrollY > 30) {

        nav.classList.add("scrolled");

    } else {

        nav.classList.remove("scrolled");

    }

}, { passive: true });


/*
    SCROLL ANIMATION

    Elementlar avval ko'rinadi.
    IntersectionObserver tayyor bo'lgandan keyin
    animatsiya bilan yashirib/chiqaradi.
*/

const elements =
    document.querySelectorAll(".reveal");


if ("IntersectionObserver" in window) {

    const observer =
        new IntersectionObserver(

            function (entries) {

                entries.forEach(function (entry) {

                    if (entry.isIntersecting) {

                        entry.target.classList.add("visible");

                        observer.unobserve(
                            entry.target
                        );

                    }

                });

            },

            {
                threshold: 0.08
            }

        );


    elements.forEach(function (element) {

        observer.observe(element);

    });

} else {

    /*
        Eski brauzer bo'lsa ham
        ma'lumotlar ko'rinadi.
    */

    elements.forEach(function (element) {

        element.classList.add("visible");

    });

}


/*
    SMOOTH ANCHORS
*/

document
.querySelectorAll('a[href^="#"]')
.forEach(function (link) {

    link.addEventListener("click", function (event) {

        const id =
            this.getAttribute("href");

        const target =
            document.querySelector(id);

        if (!target) {
            return;
        }

        event.preventDefault();

        target.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });

    });

});

</script>


</body>

</html>
"""


@app.route("/")
def home():

    return render_template_string(
        HTML,
        data=DATA
    )


if __name__ == "__main__":

    port = int(
        os.getenv("PORT", "5000")
    )

    app.run(
        host="127.0.0.1",
        port=port,
        debug=False
    )