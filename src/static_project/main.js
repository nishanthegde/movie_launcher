$(document).ready(function () {
    var table = $('#movie_user_table');
    var tableOptions = {
        'bPaginate': false,
        'bStateSave': true,
        'bStateDuration':-1
    };
    table.DataTable(tableOptions);

    $('.ui.dropdown')
        .dropdown()
    ;

    $('.message .close')
        .on('click', function () {
            $(this)
                .closest('.message')
                .transition('fade')
            location.href="./assign_movies"
            ;
        })
    ;

    $('#modal-btn').click(function () {
        $('.ui.modal')
            .modal('show')
        ;
    })
    ;
})