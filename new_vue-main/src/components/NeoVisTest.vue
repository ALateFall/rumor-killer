<template>
  <div class="myViz" style="text-align: center">
    <div class="showif" v-show="this.flag">
      <div id="viz" class="neojs"></div>
    </div>
    <div v-show="this.flag == 0" style="text-align: center; height: 610px">
      <div style="height: 300px"></div>
      <a-spin />
    </div>
    <div class="buttons">
      <a-button
        @click="this.rerender"
        style="margin-right: 17px; margin-left: 20px"
        >恢复初始</a-button
      >
      <a-button @click="this.update" style="margin-right: 17px"
        >查看更多</a-button
      >
      <a-button @click="this.getCluster" style="margin-right: 17px"
        >查看分类</a-button
      >
      <a-button @click="this.viewCluster" style="margin-right: 17px"
        >查看该类</a-button
      >
      <a-button @click="this.stabilize" style="margin-right: 17px"
        >固定图谱</a-button
      >
      <a-button @click="this.otherMovie" style="margin-right: 17px"
        >其他网站</a-button
      >
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
    }, 500);
    // this.flag = 1;
  }, //渲染
  methods: {
    stabilize() {
      this.viz.stabilize();
    },
    rerender() {
      this.flag = 0;
      this.viz.renderWithCypher(
        "MATCH p=(m:Movie)-[:has_movie] -(n:Domain)  WHERE n.name= " +
          this.url +
          " RETURN p limit 20"
      );
      // console.log("flag:", this.flag);
      setTimeout(() => {
        this.flag = 1;
      }, 200);
    },
    update() {
      this.flag = 0;
      // this.viz.clearNetwork()
      this.viz.renderWithCypher(
        "MATCH p=(m:Movie)-[:has_movie] -(n:Domain)-[r:with_title]-(t:Title),q=(n:Domain)-[:with_IP]-(i:IP)  WHERE n.name= " +
          this.url +
          " RETURN p,q limit 30"
      );
      setTimeout(() => {
        this.flag = 1;
      }, 200);
    },
    getCluster() {
      this.flag = 0 ;
      this.viz.renderWithCypher(
        "MATCH p=(i:IP)-[:with_IP]-(n:Domain)-[r:with_title]-(t:Title),q=(n:Domain)-[:in_cluster]-(c:Cluster) WHERE n.name= " +
          this.url +
          " RETURN p,q"
      );
      setTimeout(() => {
        this.flag = 1;
      }, 10);
    },
    viewCluster() {
      this.flag = 0 ;
      this.viz.renderWithCypher(
        "MATCH p=(c:Cluster)-[:in_cluster]-(n:Domain) WHERE c.name='613' RETURN p"
      );
      setTimeout(() => {
        this.flag = 1;
      }, 50);
    },
    otherMovie() {
      this.flag = 0 ;
      this.viz.renderWithCypher(
        "MATCH p=(c:Cluster)-[:in_cluster]-(n:Domain)-[:has_movie]-(m:Movie) WHERE c.name='613' RETURN p limit 30"
      );
      setTimeout(() => {
        this.flag = 1;
      }, 200);
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
          "MATCH p=(m:Movie)-[:has_movie] -(n:Domain)  WHERE n.name= " +
          this.url +
          " RETURN p limit 15",
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
        // Your after render code here
        // this.flag = 1;
        // this.flag = 1;
        // /**
        //  * 处理节点拖到问题
        //  */
        // that.viz.nodes.on('click', function(params) {
        //   // for (var i = 0; i < params.nodes.length; i++) {
        //   //   var nodeId = params.nodes[i]
        //   //   eno4jObject.nodes.update({ id: nodeId, fixed: { x: true, y: true }})
        //   //   console.log('结束')
        //   // }
        //   console.log("click")
        // })
        // eno4jObject.network.on('dragStart', function(params) {
        //   for (var i = 0; i < params.nodes.length; i++) {
        //     var nodeId = params.nodes[i]
        //     eno4jObject.nodes.update({ id: nodeId, fixed: { x: false, y: false }})
        //     console.log('开始')
        //   }
        // })
      });

      // this.viz.network.on('dragEnd', function(params) {
      //     for (var i = 0; i < params.nodes.length; i++) {
      //       var nodeId = params.nodes[i]
      //       eno4jObject.nodes.update({ id: nodeId, fixed: { x: true, y: true }})
      //       console.log('结束')
      //     }
      //   })
    },
  },
};
</script>

<style scoped>
#viz {
  height: 610px;
  width: 100%;
}
.buttons {
  padding: 5px;
}
a-button {
  margin-right: 25px;
}
</style>
