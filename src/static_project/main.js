$(document).ready(function () {
    var table = $('#movie_user_table');
    var tableOptions = {
        'bPaginate': false
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