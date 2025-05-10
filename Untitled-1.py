<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!--=============== CSS ===============-->
    <link rel="stylesheet" href="assets/css/styles.css">

    <title>Responsive portfolio website</title>
  </head>
  <body>
    <!--==================== HEADER ====================-->
    <header class="header" id="header">
      <nav class="nav container">
        <div class="nav__menu" id="nav-menu">
          <ul class="nav__list">

            <li class="nav__item">
              <a href="#home" class="nav__link active-link">Home</a>
            </li>

            <li class="nav__item">
              <a href="#about" class="nav__link">About</a>
            </li>

            <li class="nav__item">
              <a href="#projects" class="nav__link">Projects</a>
            </li>

            <li class="nav__item">
              <a href="#contact" class="nav__link">Contact</a>
            </li>
          </ul>

          <!-- closebutton -->
          <div class="nav__close" id="nav-close">
            <i class="ri-close-line"></i>
          </div>
        </div>

        <!-- Toggle button -->
        <div class="nav__toggle" id="nav-toggle">
          <i class="ri-menu-line"></i>
        </div>
      </nav>   
    </header>

    <!--==================== MAIN ====================-->
    <main class="main">
      <!--==================== HOME ====================-->
      <section class="home section" id="home">
        <div class="home__container container grid">
          <div class="home__content">
            <div class="home__data">
              <h3 class="home__subtitle">
                Hello, <span>I’m</span>
              </h3>
              <h1 class="home__title">Srinithya Kavadi</h1>
              <p class="home__description">
                "Welcome to my Portfolio. I'm a recent grauate with a passion for crafting innovative solutions!"
              </p>
            </div>

            <div class="home__social">
              <a href="https://github.com/Srinithya4f3" target="_blank" class="home__social-link">
                
              </a>
              <a href="https://www.linkedin.com/in/srinithya-kavadi/" target="_blank" class="home__social-link">
  
              </a>
            </div>
          </div>
        </div> 
      </section>

      <!--==================== ABOUT ====================-->
      <section class="about section" id="about">
        <div class="about__container container grid">
          <div class="about__data">
            <h3 class="section__subtitle">
              My <span>Intro</span>
            </h3>
            <h2 class="section__title">
              About Me
            </h2>
            <p class="about__description">
              "Greetings! lam Srinithya Kavadi. I completed my B.Tech degree specialization Electronics and communication Engineering in G Pullaiah college of engineering and technology in Kurnool. I am a recent graduate 2024.
              
              Let's explore, experiment, and engineer the future together! Welcome to my realm of creation, innovation, and infinite possibilities."
            </p>

            <a href="#contact" class="button">Contact Me</a>
          </div>

      <!--==================== SKILLS ====================-->
      <section class="skills section">
        <div class="skills__container container grid">
          <div class="skills__data">
            <h2 class="section__title">
              My Skills
            </h2>
            <a href="#projects" class="button">See Projects</a>
          </div>


          <div class="skills__content">
            <ol class="skills__group">
              <li class="skills__item">Python</li>
              <li class="skills__item">Java</li>
              <li class="skills__item">Git & Github</li>
            </ol>
          </div>
          
        </div>
      </section>

      <!--==================== PROJECTS ====================-->
      <section class="projects section" id="projects">
        <h3 class="section__subtitle">
          My <span>Projects</span>
        </h3>
        <div class="projects__container container grid">
          
          <article class="projects__card">
            <br>
            <div class="projects__modal">
              <span class="projects__subtitle">Emovision: Deep Learning for Real Time Facial Expression Recognition/n </span>
            </div>
            </article>
          </br>
          </article>

          <article class="projects__card">
            <br>
            <div class="projects__modal">
              <span class="projects__subtitle">Water Facilities and Drinking Water Availability</span>
            </div>
            </br>
          </article>

          <article class="projects__card">
            <br>
            <div class="projects__modal">
              <span class="projects__subtitle">HUMAN GENETICS </span>
            </div>
            </br>
          </article>

          <article class="projects__card">
            <br>
            <div class="projects__modal">
              <span class="projects__subtitle">TACHOMETER</span>
            </div>
          </br>
          </article>
        </div>
      </section>

      <!--==================== CONTACT ====================-->
      <section class="contact section" id="contact">
        <h3 class="section__subtitle">
          Get In <span>Touch</span>
        </h3>
        
        <h2 class="section__title">
          Contact Me
        </h2>
        
        <div class="contact__container container grid">
          <form action="" class="contact__form" id="contact-form">
            <div class="contact__group">
              <input type="text" name="user_name" required placeholder="Enter your name"
               class="contact__input">
              <input type="email" name="user_email" required placeholder="Enter your email"
               class="contact__input">
            </div>>

            <p class="contact__message" id="contact-message"></p>

            <button type="submit" class="button contact__button">
              Send Message
            </button>
          </form>
        </div>
      </section>
    </main>

    <!--==================== FOOTER ====================-->
    <footer class="footer">
      <div class="footer__container container grid">
        <div>
          <h1 class="footer__title">
            Srinithya <span>Kavadi</span>
          </h1>

          <h2 class="footer__education">
            Fresher
          </h2>
        </div>

        <div class="footer__social">
          <a href="https://twitter.com/home" target="_blank" class="footer__social-link">
            <i class="ri-twitter-line"></i>
          </a>
        </div>

        <span class="footer__copy">
          &#169; Copyright Srinithya. All rights reserved
        </span>
      </div>   
    </footer>

    <!--========== SCROLL UP ==========-->
    <a href="#" class="scrollup" id="scroll-up">
      <i class="ri-arrow-up-line"></i>
    </a>
    

    <!--=============== SCROLLREVEAL ===============-->
    <script src="assets/js/scrollreveal.min.js"></script>

    <!--=============== EMAIL JS ===============-->
    <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
    

    <!--=============== MAIN JS ===============-->
    <script src="assets/js/main.js"></script>
  </body>
</html>