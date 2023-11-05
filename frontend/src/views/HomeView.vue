<template>
    <div class="home">
        <el-container>
            <el-input placeholder="Search" prefix-icon="el-icon-search" size="large" style="width: 100%" v-model="searchInput"></el-input>
        </el-container>
        <el-container direction="vertical">
            <el-row justify="space-evenly" v-for="(games, idx) in filteredGames" :key="idx"> 
                <el-col :span="6" v-for="(game, idx) in games" :key="idx">
                    <GameCard :game="game" />
                </el-col>
            </el-row>
        </el-container>
        <!--GameCard :game="{picture: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.VXDSpudGCV9oSOQ4Jd-8jQHaLH%26pid%3DApi&f=1&ipt=89058b7c13ec02fa4311fc9040646c8f090a77cef3459f85bb4bbd36b1582a0a&ipo=images', name: 'Dragon Ball Z', price: '$27', discount : '-13%', howLongToBeat: '15h', metacritic: 50}"></GameCard-->
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import GameCard from '@/components/GameCard.vue'; // @ is an alias to /src
import axios from 'axios';
import Game from '@/game';


export default defineComponent({
  name: 'HomeView',
  components: {
    GameCard,
  },
  data(){
    return {
      games: new Array<Game>(),
      searchInput: '',
    }
  },
  async mounted() {
    try {
        await this.getGames();
    } catch(error) {
        console.log(error);
    }

  },
  methods: {
    async getGames() {
        const response = await axios.get<Game[]>('http://127.0.0.1:5000/games');
        this.games = response.data;
    },
    splitArrayChunks<T>(array: T[], n: number): T[][] {
        const result: T[][] = [];
        for (let i = 0; i < array.length; i += n) {
            result.push(array.slice(i, i + n));
        }
        return result;
    }

  },
  computed: {
    filteredGames(): Game[][] {
        let result =  this.games.filter((game) => {
            return game.name.toLowerCase().includes(this.searchInput.toLowerCase());
        });
        return this.splitArrayChunks(result, 3);
    }
  }

});
</script>

<style lang="css" scoped>
.el-row {
    margin-bottom: 20px;
}
.el-row:last-child {
    margin-bottom: 0;
}

</style>
