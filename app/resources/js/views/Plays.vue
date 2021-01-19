<template>
  <div>
    <!-- {{message}} -->
    {{ plays }}
  </div>
</template>


<script>
import axios from "axios";

export default {
  name: "Plays",
  components: {
    Plays,
  },
  data() {
    return {
      plays: null,
    };
  },
  mounted() {
    axios.get("http://localhost:8000/api/plays").then((response) => {
      console.log(response);
      this.plays = response.data;
    });
  },
};

</script>