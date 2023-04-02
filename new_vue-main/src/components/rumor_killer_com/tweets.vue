<template>
    <a-row :gutter="24">
        <div v-infinite-scroll="handleInfiniteOnLoad" class="demo-infinite-container" :infinite-scroll-disabled="busy"
            :infinite-scroll-distance="10">
            <a-list :data-source="data">
                <a-list-item slot="renderItem" slot-scope="item">
                    <a-list-item-meta :description="item.create_time">
                        <a slot="title">{{ item.user_name }}</a>
                        <a-avatar slot="avatar" :src="url" />
                    </a-list-item-meta>
                    {{ item.tweet_text }}
                </a-list-item>
                
                <div v-if="loading && !busy" class="demo-loading-container">
                    <a-spin />
                </div>
            </a-list>
        </div>
    </a-row>
</template>
  
  
<script>

import tweetURL from "../../assets/img/tweet.png"
import infiniteScroll from "vue-infinite-scroll";

export default {
    name: "tweets",
    directives: { infiniteScroll },
    components: {

    },
    data() {
        return {
            data: [],
            url: tweetURL,
            loading: false,
            busy: false,
        };
    },

    beforeMount() {
        this.fetchData();
    },

    methods: {
        async fetchData(callback) {
            await this.axios
                .post("http://localhost:5000/tweets/getTrendingTweets")
                .then(response => {
                    // this.data = data
                    console.log(response);
                    for (var i = 0; i < 10; i++) {
                        this.data.push(response.data[i]);
                    }
                })
                .catch(error => {
                    console.log(error);
                });
        },

        handleInfiniteOnLoad() {
            const data = this.data;
            this.loading = true;
            if (data.length > 500) {
                this.$message.warning("没有更多了~");
                this.busy = true;
                this.loading = false;
                return;
            }
            this.fetchData((res) => {
                this.loading = false;
            });
        },


    },
};
</script>

<style>
.demo-infinite-container {
    /* border: 1px solid #e8e8e8; */
    /* border-radius: 4px; */
    overflow: auto;
    padding: 8px 24px;
    height: 460px;
}

.demo-loading-container {
    position: absolute;
    bottom: 40px;
    width: 100%;
    text-align: center;
}
</style>