<template>
  <div>
    <a-row>
      <a-col></a-col>
    </a-row>
    <a-row>
      <!-- <transition-group> -->
        <a-col
          v-for="(item, index) in working"
          :key="index"
          class="cols"
          :span="6"
          offset="1"
        >
          <working-card :TaskName="item" />
        </a-col>
      <!-- </transition-group> -->
    </a-row>
    <a-row style="margin-top: 25px">
      <a-col :span="24"><a-divider /></a-col>
    </a-row>
    <a-row>
      <transition-group tag="">
        <a-col
          v-for="item in done"
          :key="item"
          class="cols"
          :span="6"
          offset="1"
        >
          <done-card @func="doneClick" :TaskName="item" />
        </a-col>
      </transition-group>
    </a-row>
  </div>
</template>

<script>
import WorkingCard from "../components/WorkingCard.vue";
import DoneCard from "../components/DoneCard.vue";

export default {
  components: { WorkingCard, DoneCard },

  data(){
    return{
        working:[],
        done:[],
        temp:[],
    }
  },

  beforeMount() {
    this.getData();
  },

  methods:{
    doneClick(value) {
      console.log(value.TaskName);
      console.log(this.done);
      this.temp = this.done.concat();
      for (var i = 0; i < this.temp.length; i++) {
        this.done.pop();
        // console.log(this.done);
      }
      for (var i = 0; i < this.temp.length; i++) {
        if (this.temp[i] != value.TaskName) {
          this.done.push(this.temp[i]);
          // console.log(this.done);
        }
      }
      console.log(this.done);
    },

    getData() {
      this.axios
        .post("http://localhost:5000/apiRequestSender/query/getTimerRemain",{a:1})
        .then((response)=>{
          console.log(response.data.data);
          for (var i = 0; i < response.data.data.length; i++) {
            if (response.data.data[i].remain <= 0) {
              this.done.push(response.data.data[i].name);
            } else {
              this.working.push(response.data.data[i].name);
            }
          }
          console.log("working:", this.working);
          console.log("done:", this.done);
        });
    }
  }

  // setup() {





  //   return { working, done, getData, doneClick };
  // },
};
</script>


<style scoped>
.cols {
  margin-top: 40px;
}

.v-item {
  list-style-type: none;
  /**
	 * 可以在v-enter-active和v-move中分别用transition过渡，也可以在item中用transition，包含了这两项
	 * 要用all不用transform，有可能是因为splice删除效果不是transform
	 */
  transition: all 1s;
}
.v-enter-active,
.v-leave-active {
  transition: all 1s;
}
.v-move {
  transition: all 1s;
}
.v-enter,
.v-leave-to {
  opacity: 0;
  transform: translateY(20px);
}
.v-leave-active {
  position: absolute;
}
</style>