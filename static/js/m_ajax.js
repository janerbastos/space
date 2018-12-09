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
    $('#error').html('');
	$.ajax({
		url: url,
		type : "GET",
        data : param,
        contentType : "application/josn; charset=utf-8",
        success : function(data, status) {
        	modal.find('.modal-body').html(data.result);
        },
        error : function(xhr , errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
        }
	});
};


$('#form-ajax').on('submit', function(){
    $.ajax({
        url     : $(this).attr('action'),
        type    : $(this).attr('method'),
        dataType: 'json',
        data    : $(this).serialize(),
        cache   : false,
        success : function(data, status) {
            $('.modal-body').html(data.result);
            //Atualiza o registro na tabela
            if (data.action == 'update'){
                $('#row_' + data.oid).html(data.row)
            };
            //Inclui um novo registro na tabela
            if (data.action == 'create'){
                $('#registros li:first').after(data.row);
            }

            if ( data.action == 'fechar'){
                $('#form-modal').modal('hide');
                reload("#show-pagina", data.url);
            }
            
        },
        error : function(xhr , errmsg, err) {
            console.log(xhr.status + ": " + xhr.data);
        },
    });    
    return false;
});

function reload(tag_id, url){
    $.get(url, function(data, status){
        $(tag_id).html(data.result);
    });
}

$('#btn_pesquisar').on('click', function(event){
    var url = $('#form-ajax').attr('action');
    var search = $('#txt-seach').val();
    $.get(url+'?search='+search, function(data, status){
        $('.modal-body').html(data.result);
    })
});

