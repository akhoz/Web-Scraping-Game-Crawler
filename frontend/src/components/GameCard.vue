<template>
    <router-link :to="{ name: 'GameDetail', params: { id: game.id}}">
        <el-card>
            <el-image :src="game.image" fit="cover" style="height: 20rem">
            </el-image>
            <el-text tag="h2" class="game-title">{{game.name}}</el-text>
            <el-row justify="space-evenly" >
                <el-col :span="5"><el-text tag="p" class="game-properties">${{game.price}}</el-text></el-col>
                <el-col :span="5"><el-text tag="p" class="game-properties">{{game.discount}}</el-text></el-col>
            </el-row>
        </el-card>
    </router-link>
</template>

<script lang="ts">
    import { defineComponent } from 'vue';
    export default defineComponent({
        props: {
            game: {
                type: Object,
                required: true
            }
        },

    });
</script>

<style lang="css" scoped>
/*.el-card {
    width: 20rem;
    margin: 1rem;
}*/
.game-title {
    font-size: 1.5rem;
    font-weight: bold;
}
.game-properties {
    font-size: 1.3rem;
}
</style>

