$('#form-modal').on('shown.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var titulo = button.data('titulo');
    var url = button.data('url');
    var action = button.data('action');

    var modal = $(this);
    var form = modal.find('form');

    form.attr('action', url);
    modal.find('.modal-title').html(titulo);
    modal.find('.modal-body p').html("");

    if(action=='create'){
        modal.find('.modal-body p').html("<strong>Fazendo registro de espaço para reservar.</strong>");
        param = {}
        run(url, param, modal);
    }
});

function run(url, param, modal) {
	$.ajax({
		url: url,
		type : "GET",
        data : param,
        contentType : "application/josn; charset=utf-8",
        success : function(data) {
        	 modal.find('.modal-body p').html(data.result);
        },
        error : function(xhr , errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
        }
	});
}

$('#form-ajax').on('submit', function(){
    $.ajax({
        url     : $(this).attr('action'),
        type    : $(this).attr('method'),
        dataType: 'json',
        data    : $(this).serialize(),
        cache   : false,
        success : function(data) {
            $('.modal-body p').html(data.result);
            //Atualiza o registro na tabela
            if (data.action == 'update'){
                $('#row_' + data.oid).html(data.row)
            };
            //Inclui um novo registro na tabela
            if (data.action == 'create'){
                $('#registros li:first').after(data.row);
            }
        },
        error : function(xhr , errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
        },
    });    
    return false;
});