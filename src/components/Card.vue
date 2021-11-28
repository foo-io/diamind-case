<template>
  <div class="card">
    <slot></slot>
  </div>
</template>

<style>

.card {
  background: #FFFFFF;
  box-shadow: 10px 9px 25px rgba(0, 0, 0, 0.03);
  border-radius: 10px;
  display: flex;
  flex-direction: column;
}

</style>