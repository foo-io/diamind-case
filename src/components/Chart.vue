<script>
import { Doughnut } from 'vue-chartjs'

export default {
  name: "Chart",
  extends: Doughnut,
  props: {
    item: Object
  },
  data() {
    return {
      chartData: {
        labels: [],
        datasets: [
          {
            data: [],
            backgroundColor: ['#0E6FE2', '#00A556', '#FF3D00', '#F6D43E']
          }
        ],
      },
      options: {
        responsive: false,
        maintainAspectRatio: true,
        legend: {
            position: "top",
            align: "start",
        }
      },
    }
  },
  mounted () {
    let obj = this.item;
    this.chartData.labels = Object.keys(obj);
    let values = Object.values(obj);
    let newValues = [];
    values.forEach(item => {
      let shitPercent = (item * 100).toFixed(0);
      newValues.push(shitPercent);
    })
    this.chartData.datasets[0].data = newValues;
    this.renderChart(this.chartData, this.options)
  },
}
</script>

<style>

</style>