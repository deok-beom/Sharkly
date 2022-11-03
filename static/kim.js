$(document).ready(function () {
    set_temp()
    show_comment()
});

function set_temp() {
    $.ajax({
        type: "GET",
        url: "http://spartacodingclub.shop/sparta_api/weather/seoul",
        data: {},
        success: function (response) {
            $('#temp').text(response['temp'])
        }
    })
}

function save_comment() {
    let name = $('#name').val()
    let comment = $('#add-comment').val()
    let password = $('#add-password').val()

    if (name.trim() == '') {
        alert("이름을 입력해주세요")
        return
    } else if (password.trim() == '') {
        alert("비밀번호를 입력해주세요")
        return
    } else if (comment.trim() == '') {
        alert("내용을 입력해주세요")
        return
    }

    $.ajax({
        type: 'POST',
        url: '/kim-api',
        data: {
            name_give: name,
            comment_give: comment,
            password_give: password
        },
        success: function () {
            window.location.reload()
        }
    })
}

function show_comment() {
    $.ajax({
        type: "GET",
        url: "/kim-api",
        data: {},
        success: function (response) {
            let rows = response["guestbook"]

            for (let i = 0; i < rows.length; i++) {
                let name = rows[i]['name']
                let comment = rows[i]['comment']
                let id = rows[i]['_id']

                let temp_html = `<p>${comment}</p>
                                 <input type="hidden" id="id-${i}" value="${id}">
                                         <footer class="blockquote-footer" id="c-${i}">${name}
                                            <a class="ready-a" onclick="ready_delete('${i}')" href="#" data-bs-toggle="modal" data-bs-target="#deleteModal">삭제
                                            </a><a class="ready-a" onclick="ready_update('${i}')" href="#" data-bs-toggle="modal" data-bs-target="#updateModal">수정</a>
                                         </footer>`

                $('#comment-list').append(temp_html)
            }
        }
    });
}

function ready_update($index) {
    let name = $('#c-' + $index).clone().children().remove().end().text()
    let id = $('#id-' + $index).val()
    $('#update-name').text(name)
    $('#update-id').val(id)
}

function update_comment() {
    let id = $('#update-id').val()
    let comment = $('#update-comment').val()
    let password = $('#update-password').val()

    if (password.trim() == '') {
        alert("패스워드를 입력해주세요")
        return
    } else if (comment.trim() == '') {
        alert("수정할 내용을 입력해주세요")
        return
    }

    $.ajax({
        type: 'PATCH',
        url: '/kim-api',
        data: {
            id_give: id,
            comment_give: comment,
            password_give: password
        },
        success: function (response) {
            if (!response['success']) {
                alert("비밀번호가 틀립니다.")
            } else {
                window.location.reload()
                alert("수정 완료")
            }
        }
    })
}

function ready_delete($index) {
    let name = $('#c-' + $index).clone().children().remove().end().text()
    let id = $('#id-' + $index).val()
    $('#delete-name').text(name)
    $('#delete-id').val(id)
}

function delete_comment() {
    let id = $('#delete-id').val()
    let password = $('#delete-password').val()

    if (password.trim() == '') {
        alert("패스워드를 입력해주세요")
        return
    }

    $.ajax({
        type: 'DELETE',
        url: '/kim-api',
        data: {
            id_give: id,
            password_give: password
        },
        success: function (response) {
            if (!response['success']) {
                alert("비밀번호가 틀립니다.")
            } else {
                $('#deleteModal').modal('hide')
                window.location.reload()
                alert("삭제 완료")
            }
        }
    })
}