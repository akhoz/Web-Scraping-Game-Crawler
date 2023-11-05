<template>
    <div class="common-layout">
        <el-space direction="horizontal">
            <el-card shadow="hover" style="width: 700px">
                <img class="game-image" :src="game.image" alt="game image">
                <template #header>
                    <h1>{{ game.name }}</h1>
                </template>
                <div class="items">
                    <el-tag >
                        {{ game.price }}
                    </el-tag>
                    <el-tag type="success">
                        {{ game.discount }}
                    </el-tag>
                    <el-tag type="warning">
                        Metacritic Score: {{ game.metascore }}
                    </el-tag>
                    <el-tag type="danger">
                        {{ game.tta }}
                    </el-tag>

                </div>
            </el-card>

        </el-space>
    </div>
</template>

<script lang="ts">
import axios from 'axios';
import { defineComponent } from 'vue';
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
    game: {}
    };
  },
  beforeMount() {
    this.getGameDetails();
  },
  methods: {
    async getGameDetails() {
      const response = await axios.get(`http://127.0.0.1:5000/games/${this.id}`);
      this.game = response.data;
    }
  }
});
</script>
<style scoped>
.game-image {
    width: 600px;
    height: 600px;
}

</style>

