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

    $.ajax({
        type: 'POST',
        url: '/baek-api',
        data: {
            name_give: name,
            comment_give: comment,
            password_give: password
        },
        success: function (response) {
            window.location.reload()
        }
    })
}

function show_comment() {
    $.ajax({
        type: "GET",
        url: "/baek-api",
        data: {},
        success: function (response) {
            let rows = response["guestbook"]

            for (let i = 0; i < rows.length; i++) {
                let name = rows[i]['name']
                let comment = rows[i]['comment']

                let temp_html = `<p>${comment}</p>
                                 <input type="hidden" id="id-${i}">
                                         <footer class="blockquote-footer" id="c-${i}">${name}
                                            <a class="ready-a" onclick="ready_delete('c-${i}')" href="#" data-bs-toggle="modal" data-bs-target="#deleteModal">삭제
                                            </a><a class="ready-a" onclick="ready_update('c-${i}')" href="#" data-bs-toggle="modal" data-bs-target="#updateModal">수정</a>
                                         </footer>`

                $('#comment-list').append(temp_html)
            }
        }
    });
}

function ready_update($id) {
    let name = $('#' + $id).clone().children().remove().end().text()
    $('#update-name').text(name)
}

function update_comment() {
    let name = $('#update-name').text()
    let comment = $('#update-comment').val()
    let password = $('#update-password').val()

    $.ajax({
        type: 'PATCH',
        url: '/baek-api',
        data: {
            name_give: name,
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

function ready_delete($id) {
    let name = $('#' + $id).clone().children().remove().end().text()
    $('#delete-name').text(name)
}

function delete_comment() {
    let name = $('#delete-name').text()
    let password = $('#delete-password').val()

    $.ajax({
        type: 'DELETE',
        url: '/baek-api',
        data: {
            name_give: name,
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