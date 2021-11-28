<template>
  <div class="l-filter">
    <div class="l-filter-title">
      Подберите алмазный бокс по вашим параметрам
    </div>
    <form action class="l-filter-form">
      <div class="l-grid l-grid-filter">
        <multiselect 
          v-model="values.form" 
          :options="options.forms" 
          placeholder="Форма" 
          label="value" 
          :searchable="false" 
          :show-labels="false"
        ></multiselect>
        <multiselect
          v-model="values.color" 
          :options="options.colors" 
          placeholder="Цвет" 
          label="value"
          :searchable="false" 
          :show-labels="false"
        ></multiselect>
        <multiselect
          v-model="values.size"
          :options="options.size"
          placeholder="Размер"
          label="value"
          :searchable="false"
          :show-labels="false"
        ></multiselect>
        <multiselect 
          v-model="values.light"
          :options="options.light"
          placeholder="Флуоресц."
          label="value"
          :searchable="false"
          :show-labels="false"
        ></multiselect>
      </div>
      <div class="l-filter-action">
        <button class="l-filter-button" @click.prevent="$emit('setFilter')">
          Применить
        </button>
      </div>

    </form>
  </div>
</template>

<script>
import filters from '@/data/filter.json';

export default {
  name: "CFilter",
  data() {
    return {
      values: {
        form: null,
        color: null,
        size: null,
        light: null
      },
      options: filters
    }
  }
}
</script>

<style>
.l-filter {
  display: flex;
  flex-direction: column;
  padding: 10px 20px 30px;
  height: 100%;
}
.l-filter-title {
  font-size: 18px;
  line-height: 24px;
  color: #929292;
  margin-bottom: 30px;
}
.l-grid-filter {
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 10px;
}
.l-filter .multiselect__option--highlight {
  background-color: #75B3F7;
}
.l-filter .multiselect__tags,
.l-filter .multiselect__input, .l-filter .multiselect__single {
  background-color: #EFF3F3;
}
.l-filter-action {
  display: flex;
  margin-top: auto;
  justify-content: flex-end;
}
.l-filter-button {
  background: #0B77EF;
  border-radius: 5px;
  font-size: 16px;
  line-height: 20px;
  color: #FFFFFF;
  padding: 10px 30px;
  cursor: pointer;
  border: 0;
}
.l-filter-form {
  display: flex;
  flex-direction: column;
  height: 100%;
}
.l-filter .multiselect__tags {
  font-size: 16px;
}
.l-filter .multiselect__placeholder {
    padding-top: 0px;
    line-height: 20px;
}
</style>