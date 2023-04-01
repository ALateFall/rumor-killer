<template>
  <div class="myViz" style="text-align: center">
    <div class="showif" v-show="this.flag">
      <div id="viz" class="neojs"></div>
    </div>
    

    <div v-show="this.flag == 0" style="text-align: center; height: 445px">
      <div style="height: 210px"></div>
      <a-spin />
    </div>
    <div class="buttons" style="height: 50px text-align:left">
      <a-button
        @click="this.rerender"
        style="margin-right: 17px; margin-left: 20px"
        >恢复初始</a-button
      >
      <a-button @click="this.update" style="margin-right: 17px"
        >查看更多</a-button 
      >
      <!-- <a-button @click="this.getCluster" style="margin-right: 17px"
        >查看分类</a-button
      >
      <a-button @click="this.viewCluster" style="margin-right: 17px"
        >查看该类</a-button
      > -->
      <a-button @click="this.stabilize" style="margin-right: 17px"
        >固定图谱</a-button
      >
      <!-- <a-button @click="this.otherMovie" style="margin-right: 17px"
        >其他网站</a-button 
      >-->
      <a-input-search
        placeholder="输入查看的组织编号,获取更多信息"
        :loading="this.buttonFlag"
        v-model:value="clusterValue"
        @search="getByClusterId(clusterValue)"
        enter-button
        style="width: 40%"
      />
    </div>
  </div>
</template>

<script>
// const NeoVis = require("neovis.js");
import * as NeoVis from "neovis.js";

export default {
  components: {},
  props: ["site"],
  data() {
    return {
      viz: null, //定义一个viz对象
      flag: 0,
      url: "'4kgd.cn'",
      buttonFlag:false,
      clusterValue:""

    };
  },
  watch: {
    site: function (val, old) {
      // console.log("改变了", val, old);
      if (this.site == 2) {
        this.url = "'4kwc.com'";
      } else if (this.site == 1) {
        this.url = "'4kgd.cn'";
      }
      // console.log("url", this.site);
      this.draw();
    },
  },

  mounted() {
    if (this.site == 2) {
      this.url = "'4kwc.com'";
    }
    // console.log("url", this.site);
    this.draw();
    setTimeout(() => {
      this.flag = 1;
    }, 4000);
  }, //渲染
  methods: {
    getByClusterId(value){
      // console.log(value)
      // console.log(this.buttonFlag)
      this.$emit('func',value)
      this.buttonFlag=true
      setTimeout(function(){
        this.buttonFlag=false
        console.log("hhh",this.buttonFlag)
      },1000)
        this.buttonFlag=false

    },
    stabilize() {
      this.viz.stabilize();
    },
    rerender() {
      // this.flag = 0;
      this.viz.renderWithCypher(
        "match p=(n:Domain)-[r:in_cluster]-(c:Cluster) return p limit 150"
      );
      // setTimeout(()=>{
      //   console.log("1", this.flag);
      //   this.flag = 1;
      // }, 10000)
    },
    update() {
      // this.viz.clearNetwork()
      this.viz.updateWithCypher("match p=(c:Cluster) return c");
    },
    getCluster() {
      this.viz.renderWithCypher(
        "MATCH p=(i:IP)-[:with_IP]-(n:Domain)-[r:with_title]-(t:Title),q=(n:Domain)-[:in_cluster]-(c:Cluster) WHERE n.name= " +
          this.url +
          " RETURN p,q"
      );
    },
    viewCluster() {
      this.flag = 0;
      this.viz.renderWithCypher(
        "MATCH p=(c:Cluster)-[:in_cluster]-(n:Domain) WHERE c.name='613' RETURN p"
      );
      setTimeout(() => {
        this.flag = 1;
      }, 100);
    },
    otherMovie() {
      this.flag = 0;
      this.viz.renderWithCypher(
        "MATCH p=(c:Cluster)-[:in_cluster]-(n:Domain)-[:has_movie]-(m:Movie) WHERE c.name='613' RETURN p limit 30"
      );
      setTimeout(() => {
        this.flag = 1;
      }, 500);
    },
    draw() {
      var config = {
        container_id: "viz",
        server_url: "bolt://localhost:7687",
        server_user: "neo4j",
        server_password: "1234",
        labels: {
          //"Character": "name",
          // Character: {
          //   caption: "name",
          //   size: "pagerank",
          //   community: "community",
          //   //"sizeCypher": "MATCH (n) WHERE id(n) = {id} MATCH (n)-[r]-() RETURN sum(r.weight) AS c"
          // },
          Domain: {
            caption: "name",
            size: 2,
            community: "community",
          },
          Cluster: {
            caption: "name",
            size: 2,
          },
          Movie: {
            size: 1,
          },
        },
        relationships: {
          has_movie: {
            thickness: "weight",
            caption: true,
          },
        },
        //查询节点的语句，写成你们的
        initial_cypher:
          //   "MATCH p=(m:Movie)-[:has_movie] -(n:Domain)  WHERE n.name= " +
          //   this.url +
          //   " RETURN p limit 15",
          "match p=(n:Domain)-[r:in_cluster]-(c:Cluster) return p limit 150",
        // "MATCH p= (n:Cluster)-[:in_cluster]-(Domain)-[:has_movie]-(Movie) RETURN p LIMIT 100"
      };
      // this.viz = new NeoVis(config);
      this.viz = new NeoVis.default(config);
      this.viz.render();
      const that = this;
      const nodesArray = []; // 动态取出neo4j通过语句查询的节点集群
      const labelsArr = []; // 节点群
      const edgesArr = [];
      window.slm = this.viz;
      const eno4jObject = this.viz;
      that.viz.registerOnEvent("completed", (ab) => {
        // this.flag = 1;
      });
    },
  },
};
</script>

<style scoped>
#viz {
  height: 445px;
  width: 100%;
}
.buttons {
  padding: 5px;
}
a-button {
  margin-right: 25px;
}
</style>
