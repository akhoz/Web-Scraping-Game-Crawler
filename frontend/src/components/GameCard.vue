<template>
    <el-card>
        <el-image :src="game.picture" fit="cover" style="height: 20rem">
        </el-image>
        <el-text tag="h2">{{game.name}}</el-text>
        <el-row justify="space-evenly">
            <el-col :span="5"><el-text tag="p">{{game.price}}</el-text></el-col>
            <el-col :span="5"><el-text tag="p">{{game.discount}}</el-text></el-col>
        </el-row>
    </el-card>
</template>
<script lang="ts">
    import { defineComponent } from 'vue';
    export default defineComponent({
        data(){
            return 
        },
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
</style>

