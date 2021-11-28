<template>
  <div class="l-percent">
    <div class="l-percent-title">{{title}}</div>
    <div class="l-percent-info">
      <div class="l-percent-info-text">
        {{textValue}}
      </div>
      <div class="l-percent-info-value">
        {{newValue}}%
      </div>
    </div>
    <div class="l-percent-block">
      <div class="l-percent-line" :style="{ width: newValue + '%'}"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CPercent",
  props: {
    title: String,
    textValue: String,
    value: Number,
  },
  data() {
    return {

    }
  },
  computed: {
    newValue: function () {
      let newValue = this.value*100;
      return newValue.toFixed(0);
    }
  }
}
</script>

<style>
.l-percent {
  display: flex;
  flex-direction: column;
}
.l-percent-title {
  font-weight: bold;
  font-size: 16px;
  line-height: 20px;
  color: #242E40;
}
.l-percent-info {
  display: flex;
  justify-content: space-between;
  margin-top: 5px;
}
.l-percent-info-text {
  font-size: 16px;
  line-height: 20px;
  color: #929292;
}
.l-percent-info-value {
  font-weight: bold;
  font-size: 16px;
  line-height: 20px;
  color: #0B77EF;
}
.l-percent-block {
  background: #EFF3F3;
  border-radius: 3px;
  overflow: hidden;
  height: 4px;
  margin-top: 5px;
}
.l-percent-line {
  display: flex;
  height: 4px;
  background: #0B77EF;
  border-radius: 0 3px 3px 0;
}
</style>