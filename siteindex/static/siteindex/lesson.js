const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')


modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {

    const pk = modalBtn.getAttribute('data-pk')
    const url = modalBtn.getAttribute('data-url')
    const title = modalBtn.getAttribute('data-title')
    const lecturer = modalBtn.getAttribute('data-lecturer')
    const status = modalBtn.getAttribute('data-status')

    const precond = modalBtn.getAttribute('data-precond')
    const precond_of = modalBtn.getAttribute('data-precond-of')

    modalBody.innerHTML = `
        <div class="h4 mb-3"> 确定开始 "<b> ${title} </b>" ? </div>
        <ul>
            <li>讲师：${lecturer}</li>
            <li>学习状态：${status}</li>
            <li>前置课程：${precond}</li>
            <li>作为：${precond_of} 的前置课程</li>
        </ul>
    `
    startBtn.style.display = "inline";

    startBtn.addEventListener('click', () => {
        window.location.href = url
    })

}))

const NoPermBtns = [...document.getElementsByClassName('no-permission-button')]

NoPermBtns.forEach(NoPermBtn => NoPermBtn.addEventListener('click', () => {

    const pk = NoPermBtn.getAttribute('data-pk')
    const url = NoPermBtn.getAttribute('data-url')
    const title = NoPermBtn.getAttribute('data-title')
    const lecturer = NoPermBtn.getAttribute('data-lecturer')
    const status = NoPermBtn.getAttribute('data-status')

    const precond = NoPermBtn.getAttribute('data-precond')
    const precond_of = NoPermBtn.getAttribute('data-precond-of')

    modalBody.innerHTML = `
        <div class="h4 mb-3"> 请完成前置课程 "<b> ${precond} </b>" </div>
        <ul>
            <li>课程名称：${title}</li>
            <li>讲师：${lecturer}</li>
            <li>学习状态：${status}</li>
            <li>前置课程：${precond}</li>
            <li>作为：${precond_of} 的前置课程</li>
        </ul>
    `
    startBtn.style.display = "none";

}))
