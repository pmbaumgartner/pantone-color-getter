// .vuepress/enhanceApp.js

import VueClipboard from 'vue-clipboard2'
import VTooltip from 'v-tooltip'
import {
    FontAwesomeIcon
} from '@fortawesome/vue-fontawesome'
import {
    library
} from '@fortawesome/fontawesome-svg-core'
import {
    faCopy
} from '@fortawesome/free-regular-svg-icons'

library.add(
    faCopy,
)
export default ({
    Vue,
    options,
    router,
    siteData
}) => {
    Vue.use(VueClipboard),
        Vue.use(VTooltip),
        Vue.component('font-awesome-icon', FontAwesomeIcon)

}