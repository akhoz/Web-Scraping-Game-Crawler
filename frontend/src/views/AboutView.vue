<template>
  <div class="letters">
    <div class="letter">
      <div class="content">
        <div class="person">
          <img src="../../images/Adrian.png" alt="Adrian Villalobos" />
          <p>Adrian Villalobos</p>
        </div>
        <div class="social-media">
          <a href="https://github.com/akhoz" target="_blank">
            <img src="../../images/github.png" alt="GitHub" />
          </a>
          <a href="https://www.instagram.com/adrian_jvp25/" target="_blank">
            <img src="../../images/instagram.webp" alt="Instagram" />
          </a>
        </div>
      </div>
    </div>

    <div class="letter">
      <div class="content">
        <div class="person">
          <img src="../../images/Isaac.png" alt="Isaac Ramirez" />
          <p>Isaac Ramirez</p>
        </div>
        <div class="social-media">
          <a href="https://github.com/iZackk26" target="_blank">
            <img src="../../images/github.png" alt="GitHub" />
          </a>
          <a href="https://www.instagram.com/izackk_r/" target="_blank">
            <img src="../../images/instagram.webp" alt="Instagram" />
          </a>
        </div>
      </div>
    </div>

    <div class="letter">
      <div class="content">
        <div class="person">
          <img src="../../images/Hector.png" alt="Hector Caravaca" />
          <p>Hector Caravaca</p>
        </div>
        <div class="social-media">
          <a href="https://github.com/tuusuario" target="_blank">
            <img src="../../images/github.png" alt="GitHub" />
          </a>
          <a href="https://www.instagram.com/jordienpo" target="_blank">
            <img src="../../images/instagram.webp" alt="Instagram" />
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="css" scoped>
.letters {
  display: flex;
  justify-content: space-around;
}

.letter {
  background-size: cover;
  background-repeat: no-repeat;
  width: 300px;
  padding: 20px;
  border: 2px solid #000;
  border-radius: 10px;
  box-shadow: 5px 5px 10px #888;
  text-align: center;
  font-family: 'Arial', sans-serif;
  color: #333;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.person {
  margin: 20px 0;
}

.person img {
  width: 100px;
  border-radius: 50%;
}

.social-media {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 10px 0;
}

.social-media a {
  margin: 0 5px;
}

.social-media img {
  width: 30px;
}

.social-media img:hover {
  transform: scale(1.2);
}
</style>
