const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {

    const pk = modalBtn.getAttribute('data-pk')
    const title = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    const precond = modalBtn.getAttribute('data-precond')
    const precond_of = modalBtn.getAttribute('data-precond-of')

    modalBody.innerHTML = `
        <div class="h4 mb-3"> 确定开始 "<b> ${title} </b>" ? </div>
        <ul>
            <li>前置课程：${precond}</li>
            <li>作为：${precond_of} 的前置课程</li>
            <li>问题数量：${numQuestions}</li>
            <li>及格分数：${scoreToPass} %</li>
            <li>预计时间：${time} 分钟</li>
        </ul>
    `
    startBtn.style.display = "inline";

    startBtn.addEventListener('click', () => {
        window.location.href = url + pk
    })

}))

const NoPermBtns = [...document.getElementsByClassName('no-permission-button')]

NoPermBtns.forEach(NoPermBtn => NoPermBtn.addEventListener('click', () => {

    const title = NoPermBtn.getAttribute('data-quiz')
    const precond = NoPermBtn.getAttribute('data-precond')
    const precond_of = NoPermBtn.getAttribute('data-precond-of')

    modalBody.innerHTML = `
        <div class="h4 mb-3"> 请完成前置课程 "<b> ${precond} </b>" </div>
        <ul>
            <li>课程：${title}</li>
            <li>前置课程：${precond}</li>
            <li>作为：${precond_of} 的前置课程</li>
        </ul>
    `

    startBtn.style.display = "none";

}))
