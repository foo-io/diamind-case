<template>
  <div id="app">
    <section class="l-section">
      <Title>Подобрать бокс</Title>
      <div class="l-grid l-grid-first-block">
        <Card>
          <div class="l-card-title">
            <div class="l-card-title-icon">
              <img src="@/assets/icon-filter.svg" alt="Filter">
            </div>
            <div class="l-card-title-value">
              Фильтр
            </div>
          </div>
          <CFilter @setFilter="setFilter"></CFilter>
        </Card>
        <Card>
          <div class="l-best">
            <div class="l-grid l-grid-second-block">
              <div class="l-best-aside">
                <div class="l-best-photo">
                  <img src="https://via.placeholder.com/400x400" alt="Photo">
                </div>
                <a href="#" class="l-button">Оформить</a>
              </div>
              <div class="l-best-information">
                <div class="l-card-title-value">
                  Бокс №{{ selectedBox.number }}
                </div>
                <div class="l-card-subtitle-value">
                  Максимальное содержимое
                </div>
                <div class="l-best-information-datasets">
                  <div class="l-grid l-grid-three-block">
                    <CPercent title="Цвет" :text-value="selectedBox.color.text" :value="selectedBox.color.value"></CPercent>
                    <CPercent title="Размер" :text-value="selectedBox.size.text" :value="selectedBox.size.value"></CPercent>
                    <CPercent title="Флуоресценция" :text-value="selectedBox.light.text" :value="selectedBox.light.value"></CPercent>
                    <CPercent title="Форма" :text-value="selectedBox.form.text" :value="selectedBox.form.value"></CPercent>
                    <div class="l-best-number">
                      <div class="l-best-number-title">
                        Вес
                      </div>
                      <div class="l-best-number-value">
                        {{ selectedBox.weight }} ct.
                      </div>
                    </div>
                    <div class="l-best-number">
                      <div class="l-best-number-title">
                        Стоимость
                      </div>
                      <div class="l-best-number-value">
                        {{ selectedBox.cost }} у.е.
                      </div>
                    </div>
                  </div>
                </div>
                <div class="l-best-showmore">
                  <button class="l-showmore" @click="isShowmore = !isShowmore">
                    <span>{{!isShowmore ? 'Подробнее' : 'Скрыть'}}</span>
                    <img src="@/assets/icon-arrow.svg" alt="Arrow" :class="{'is-active': isShowmore}">
                  </button>
                </div>
              </div>
            </div>
          </div>
        </Card>
      </div>
    </section>
    <transition name="fade">
      <section class="l-section" v-if="isShowmore">
        <Card>
          <div class="l-charts">
            <div class="l-grid l-grid-five-block">
              <div v-for="(item, idx) in selectedBox.parameters" :key="idx">
                <div class="l-chart-title">{{getTextByKey(idx)}}</div>
                <Chart :item="item" style="position: relative; margin: 0 auto;" :width="290"></Chart>
              </div>
            </div>
          </div>
        </Card>
      </section>
    </transition>
    <section class="l-clusters">
      <div class="l-section">
        <Title>Список боксов</Title>

        <div class="l-boxes">
          <div class="l-grid l-grid-four-block">
            <CBox v-for="box in clusters" :key="box.id" :item="box" :class="{'is-active': box.id === selected}" @changeSelect="changeSelect"></CBox>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Title from '@/components/Title';
import CFilter from '@/components/CFilter';
import Card from '@/components/Card';
import CPercent from './components/CPercent';
import CBox from './components/CBox';
import Chart from './components/Chart';

import list from '@/data/data.json';

export default {
  name: 'App',
  components: {
    Card, Title, CFilter,
    CPercent, CBox, Chart
  },
  data() {
    return {
      isShowmore: false,
      selected: 0,
      clusters: list.clusters,
    }
  },
  computed: {
    selectedBox: function () {
      let boxId = this.selected;
      let boxNumber = boxId + 1;
      let boxObject = this.clusters[boxId];

      let color = boxObject.parameters['Цвет'];
      let size = boxObject.parameters['Размер'];
      let light = boxObject.parameters['Флуоресценция'];
      let form = boxObject.parameters['Форма'];
      let cost = boxObject.parameters['Стоимость'];
      let weight = boxObject.parameters['Вес'];
      let count = boxObject.parameters['Количество'];

      const getMaxKey = obj => {
        const value = Math.max.apply(null, Object.values(obj));
        const text = Object.keys(obj).find(key => obj[key] === value);
        return {
          text, value
        }
      }

      let boxInfo = {
        color: getMaxKey(color),
        size: getMaxKey(size),
        light: getMaxKey(light),
        form: getMaxKey(form),
      }

      return {
        id: boxId,
        number: boxNumber,
        ...boxInfo,
        parameters: {
          color,
          size,
          light,
          form
        },
        cost,
        weight,
        count
      }
    },
  },
  methods: {
    changeSelect: function (itemId) {
      this.selected = itemId;
    },
    randomInteger: function (min, max) {
      let rand = Math.random() * (max - min) + min;
      return Math.round(rand);
    },
    setFilter: function () {
      let rand = this.randomInteger(0, this.clusters.length-1);

      this.selected = rand;
    },
    getTextByKey: function (idx) {
      if (idx === 'color')
        return 'Цвет'
      if (idx === 'size')
        return 'Размер'
      if (idx === 'form')
        return 'Форма'
      if (idx === 'light')
        return 'Флуоресценция'
    }
  },
  watch: {
    selectedBox() {
      this.isShowmore = false;
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: Roboto, Arial, sans-serif;
}
html {
  background: #F7F8FC;
}
#app {
  color: #2c3e50;
}
.l-section {
  max-width: 1380px;
  padding: 0 30px;
  margin: 30px auto;
}
.l-section + .l-section {
  margin-top: 30px;
}
.l-grid {
  display: grid;
}
.l-grid-first-block {
  grid-template-columns: 6fr 9fr;
  grid-gap: 30px;
}
.l-grid-second-block {
  grid-template-columns: auto 1fr;
  grid-gap: 20px;
}
.l-grid-three-block {
  grid-template-rows: repeat(3, 1fr);
  grid-template-columns: repeat(2, 1fr);
  grid-auto-flow: column;
  grid-gap: 20px 30px;
}
.l-grid-four-block {
  grid-template-columns: repeat(5, 1fr);
  grid-gap: 30px;
}
.l-grid-five-block {
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 30px;
}
.l-card-title {
  display: flex;
  padding: 30px 20px 0;
}
.l-card-title-icon {
  display: flex;
  margin-right: 15px;
}
.l-card-title-value {
  font-weight: 700;
  font-size: 20px;
  line-height: 23px;

  color: #242E40;
}
.l-best {
  padding: 30px 20px;
}
.l-best-photo {
  width: 282px;
  height: 282px;
  overflow: hidden;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 30px;
}
.l-best-photo img {
  object-fit: cover;
}
.l-card-subtitle-value {
  font-size: 18px;
  line-height: 20px;
  color: #929292;
  margin-top: 10px;
}
.l-best-information-datasets {
  margin-top: 20px;
}
.l-button {
  background: #0B77EF;
  border-radius: 5px;
  display: flex;
  font-size: 16px;
  line-height: 20px;
  color: #FFFFFF;
  align-content: center;
  justify-content: center;
  text-decoration: none;
  padding: 10px 30px;
}
.l-best-aside {
  display: flex;
  flex-direction: column;
}
.l-best-number-title {
  font-size: 16px;
  line-height: 20px;
  text-align: right;
  color: #929292;
}
.l-best-number-value {
  font-size: 28px;
  line-height: 24px;
  text-align: right;
  color: #242E40;
  margin-top: 10px;
}
.l-best-showmore {
  display: flex;
  justify-content: flex-end;
  margin-top: auto;
}
.l-showmore {
  font-size: 16px;
  line-height: 20px;
  color: #469AF7;
  border: 0;
  padding: 0;
  background: none;
  cursor: pointer;
}
.l-showmore span {
  margin-right: 15px;
}
.l-best-information {
  display: flex;
  flex-direction: column;
}
.l-showmore img {
  transition: transform .2s ease-out;
}
.l-showmore img.is-active {
  transform: rotate(180deg);
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
.l-clusters {
  background: #fff;
  margin-top: 70px;
  padding: 40px 0;
}
.l-clusters .l-section {
  margin-top: 0;
  margin-bottom: 0;
}
.l-charts {
  padding: 30px 20px;
}
.l-chart-title {
  font-weight: bold;
  font-size: 16px;
  line-height: 20px;
  color: #242E40;
  margin-bottom: 20px;
}
</style>
