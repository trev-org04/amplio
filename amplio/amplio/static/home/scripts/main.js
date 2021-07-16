var scrollWrapper
var rooturl
var layersImage
window.addEventListener('load', () => {
    layersImage = document.getElementsByClassName('headsection-sub-scroll-img')[0].children[0]
    scrollWrapper = document.getElementsByClassName('headsection-sub-scroll-wrapper-content-scrollable')[0]
    document.getElementById('nextbutton').addEventListener('click', () => {
        var offset = document.getElementsByClassName('headsection-scrollnode')[0].offsetWidth
        if (getSnapPosition() == 3) {
            scrollWrapper.scrollTo({left: 0, behavior: 'smooth'})
        }
        else {
            scrollWrapper.scrollTo({left: scrollWrapper.scrollLeft + offset, behavior: 'smooth'})
        }
    })

    rooturl = layersImage.src

    updatePositionIndicator(getSnapPosition())
    scrollWrapper.addEventListener('scroll', () => updatePositionIndicator(getSnapPosition()))

    scaleHeaderSection()
})

function getSnapPosition() {
    let offset = document.getElementsByClassName('headsection-scrollnode')[0].offsetWidth
    let totalWidth = offset * 3
    return Math.round((scrollWrapper.scrollLeft / totalWidth) * 3 + 1)
}

function updatePositionIndicator(positon) {
    let indicators = document.getElementsByClassName('headsection-scrollpositionindicator')
    for (let index = 0; index < indicators.length; index++) {
        const element = indicators[index];
        element.className = 'headsection-scrollpositionindicator'
    }
    indicators[positon - 1].classList.add('headsection-scrollpositionindicator-selected')

    updateRootUrl(positon)
}

function updateRootUrl(index) {
    let numPos = rooturl.indexOf('.svg') - 1
    layersImage.src = layersImage.src.substring(0, numPos) + index + '.svg'
}

window.addEventListener('resize', () => scaleHeaderSection())

function scaleHeaderSection() {
    let header = document.getElementsByClassName('headsection-top')[0]
    let decalHeight = document.getElementsByClassName('headsection-sub-scroll-img')[0].children[0].offsetHeight
    if (window.innerWidth > 800) {
        header.style.minHeight = (window.innerHeight + decalHeight / 2).toString() + 'px'
    } else {
        header.style.minHeight = 'auto'
    }
}