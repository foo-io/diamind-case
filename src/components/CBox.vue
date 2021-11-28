<template>
  <button class="l-box" @click="$emit('changeSelect', item.id)">
    <div class="l-box-title">
      Бокс
    </div>
    <div class="l-box-value">
      №{{ item.id + 1 }}
    </div>
    <img src="@/assets/diamond.png" alt="" class="l-box-image">
  </button>
</template>

<script>
export default {
  name: "CBox",
  props: {
    item: Object
  },
}
</script>

<style>
.l-box {
  background: #044B9B;
  box-shadow: 10px 9px 25px rgba(0, 0, 0, 0.05);
  border-radius: 10px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  height: 150px;
  border: 0;
  cursor: pointer;
  position: relative;
  transition: background-color .2s ease-out, opacity .2s ease-out;
}
.l-box-title {
  font-weight: 500;
  font-size: 20px;
  line-height: 23px;
  color: #75B3F7;
}
.l-box-value {
  font-weight: bold;
  font-size: 50px;
  line-height: 59px;
  color: #FFFFFF;
  margin-top: 5px;
}
.l-box.is-active {
  background-color: #0B77EF;
}
.l-box.is-active .l-box-image {
  opacity: 1;
}
.l-box-image {
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  opacity: .8;
}
</style>