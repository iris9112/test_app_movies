
$(document).ready(async function () {
    let movies = await fetch('/movies/movie')
    movies = await movies.json()

    let template = '';
    movies.results.map(movie => {
        template += `${movie.id} ${movie.title} <br><br>`;
        template += ` <button type="button" data-id="${movie.id}" class="btn btn-primary detail">Detalle</button>`
        template += ` <button type="button" data-id="${movie.id}" class="btn btn-success update" data-toggle="modal" data-target="#modalUpdate">Actualizar</button>`
        template += ` <button type="button" data-id="${movie.id}" class="btn btn-danger detele">Eliminar</button> <br><br>`
    })
    $('#movies-list').html(template);

});

$(document).on('click', '.detail', async function(){
    let movie = await fetch('/movies/movie/'+$(this).data('id'))
    movie = await movie.json()

    let template = '';
    template += `${movie.id} ${movie.title} ${movie.year} ${movie.summary} ${movie.poster} ${movie.categories} ${movie.keywords}<br><br>`;

    $('#detail-list').html(template);
});

$(document).on('click', '.update', async function(){
    let movie = await fetch('/movies/movie/'+$(this).data('id'))
    movie = await movie.json()

    let form = '';
    console.log(movie);
    form += `
    <form action="" method="post">
    <div class="form-group">
        <label>title:</label>
        <input type="text" class="form-control" id="title" name="title" value="${movie.title}">
    </div>
    <div class="form-group">
        <label>year:</label>
        <input type="number" class="form-control" id="year" name="year" value="${movie.year}">
    </div>
    <div class="form-group">
        <label>summary:</label>
        <input type="text" class="form-control" id="summary" name="summary" value="${movie.summary}">
    </div>
    <div class="form-group">
        <label>poster:</label>
        <input type="text" class="form-control" id="poster" name="poster" value="${movie.poster}">
    </div>
    <div class="form-group">
        <label>categories:</label>
        <input type="text" class="form-control" id="categories" name="categories" value="${movie.categories}">
    </div>
    <div class="form-group">
        <label>keywords:</label>
        <input type="text" class="form-control" id="keywords" name="keywords" value="${movie.keywords}">
    </div>
    
    <input type="submit" class="btn btn-default" value="Submit">

    </form>
    `;

    $('#formUpdate').html(form);

});

