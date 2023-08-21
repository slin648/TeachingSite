const url = window.location.href
const quizBox = document.getElementById('quiz-box')

$.ajax({
    type: 'GET',
    url: `${url}/data/`,
    success: function (response) {

        data = response.data
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)) {
                //标题
                quizBox.innerHTML += `
                    <hr>
                    <div class="card-header text-white bg-dark py-2 px-3"><b>${question}</b></div>
                    <br>
                `
                answers.forEach(answer => {
                    //问题的radio选项点和答案lable
                    quizBox.innerHTML += `
                    <div>
                        <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                        <lable for ="${question}"> ${answer} </lable>
                    </div>
                `
                })
            }
        });
    },
    error: function (error) {
        console.log(error)
    }
})

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
    //获取选择的选项并保存至elements
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el => {
        if (el.checked) {
            data[el.name] = el.value
        }
        else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })

    $.ajax({
        type: 'POST',
        url: `${url}/save/`,
        data: data,
        success: function (response) {

            //提交答案后清除题目区域
            quizForm.innerHTML = `<hr>`

            const results = response.results
            results.forEach(res => {
                const result_div = document.createElement("div")

                for (const [question, answer] of Object.entries(res)) {

                    result_div.innerHTML += question
                    const container = ['container', 'p-3', 'text-light', 'h3']
                    result_div.classList.add(...container)

                    if (answer == 'not_answered') {
                        result_div.innerHTML += ' -- 未作答'
                        result_div.classList.add('bg-danger')
                    }
                    else {
                        const ans = answer['answered']
                        const correct = answer['correct_answer']

                        if (ans == correct) {
                            result_div.classList.add('bg-success')
                            result_div.innerHTML += ` -- 回答正确：${ans}`
                        }
                        else {
                            result_div.classList.add('bg-danger')
                            result_div.innerHTML += ` -- 正确答案：${correct} `
                            result_div.innerHTML += `; 而您选了：${ans}`
                        }
                    }
                }
                quizForm.append(result_div)
            });

            let passed = "";
            if (response.passed == true) {
                passed = '通过'
            }
            else {
                passed = '未通过'
            }
            quizForm.innerHTML += `
                <hr>
                <h4>得分：${response.score}</h4>
                <h4>是否通过：${passed}</h4>
            `
        },
        error: function (error) {
            console.log(error)
        }
    })
}

quizForm.addEventListener('submit', e => {
    e.preventDefault()
    //调用上面的函数发送数据
    sendData()
})
