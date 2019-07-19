<table>
<thead><th>Year</th><th>Color</th><th>Hex</th><th>RGB</th><th>HSL</th><th>Black Text</th><th>White Text</th></thead>
<tbody>
<tr v-for="i in items">
    <td>{{i.year}}</td>
    <td>{{i.color}}</td>
    <ColorData :color="i.hex" />
    <ColorData :color="i.rgb" />
    <ColorData :color="i.hsl" />
    <Swatch :bgcolor="i.hex" fc="rgb(0,0,0)" text="etaoin shrdlu"/>
    <Swatch :bgcolor="i.hex" fc="rgb(255,255,255)" text="etaoin shrdlu"/>
</tr>
</tbody>
</table>


<script>
import { sort } from 'fast-sort';
import data from './colors.json';

const d = data;

export default {
  data () {
      return {
          items: d
      }
  }
}
</script>
