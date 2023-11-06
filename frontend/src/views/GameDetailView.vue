<template>
    <div class="container">
        <div class="product-image">
            <img :src="game.image" class="game-image" height="300"/>
        </div>
        <div class="product-info">
            <!-- Redirect game name to game link -->
            <a :href="game.link"><h1>{{ game.name }}</h1></a>
            <p>Price: ${{ game.price }}</p>
            <p>Discount: {{ game.discount }}</p>
            <p>Metascore: {{ game.metascore }}</p>
            <p>Time to achieve: {{game.tta}}</p>
        </div>
    </div>
</template>

<script lang="ts">
import axios from 'axios';
import { defineComponent } from 'vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.js';
import Game from '@/game';

export default defineComponent({
  name: 'GameDetailView',
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
    game: {} as Game
    };
  },
  beforeMount() {
    this.getGameDetails();
  },
  methods: {
    async getGameDetails() {
      const response = await axios.get(`http://127.0.0.1:5000/games/${this.id}`);
      this.game = response.data;
      console.log(this.game);
    },
    redirectToGame() {
        window.open(this.game.link, '_blank');
    }
  }
});
</script>
<style scoped>

.product-image {
    float: left;
    box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.75);
}
.product-info {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
</style>

