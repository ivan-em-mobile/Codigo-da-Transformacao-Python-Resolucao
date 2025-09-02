from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

# 1. Inicialização do aplicativo Flask
app = Flask(__name__)

# 2. Conexão e Inicialização do Banco de Dados
def init_db():
    """
    Cria as tabelas 'usuarios' e 'posts' no banco de dados se elas ainda não existirem.
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            data_criacao TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Chama a função para garantir que as tabelas existem
init_db()

# 3. Rotas do Servidor
@app.route('/saudacao', methods=['GET'])
def saudacao():
    """
    Rota que retorna uma mensagem de saudação.
    """
    return "Olá! Bem-vindo ao meu servidor Flask!"

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    """
    Rota para cadastrar um novo usuário no banco de dados.
    Espera um JSON com 'nome' e 'email'.
    """
    if not request.is_json:
        return jsonify({"erro": "O corpo da requisição deve ser JSON"}), 400
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    if not nome or not email:
        return jsonify({"erro": "Nome e e-mail são obrigatórios"}), 400
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"erro": "Este e-mail já está cadastrado"}), 409
    except Exception as e:
        return jsonify({"erro": f"Ocorreu um erro: {e}"}), 500

@app.route('/posts', methods=['POST'])
def criar_post():
    """
    Cria um novo post no blog.
    Espera um JSON com 'titulo' e 'conteudo'.
    """
    if not request.is_json:
        return jsonify({"erro": "O corpo da requisição deve ser JSON"}), 400
    dados = request.get_json()
    titulo = dados.get('titulo')
    conteudo = dados.get('conteudo')
    if not titulo or not conteudo:
        return jsonify({"erro": "Título e conteúdo são obrigatórios"}), 400
    data_criacao = datetime.now().isoformat()
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO posts (titulo, conteudo, data_criacao) VALUES (?, ?, ?)",
                       (titulo, conteudo, data_criacao))
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Post criado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"erro": f"Ocorreu um erro: {e}"}), 500

@app.route('/posts', methods=['GET'])
def listar_posts():
    """
    Lista todos os posts do blog.
    """
    posts = []
    try:
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts")
        posts_db = cursor.fetchall()
        for post in posts_db:
            posts.append(dict(post))
        conn.close()
        return jsonify(posts), 200
    except Exception as e:
        return jsonify({"erro": f"Ocorreu um erro: {e}"}), 500

@app.route('/posts/<int:post_id>', methods=['GET'])
def ler_post(post_id):
    """
    Retorna um post específico pelo seu ID.
    """
    try:
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
        post = cursor.fetchone()
        conn.close()
        if post is None:
            return jsonify({"erro": "Post não encontrado"}), 404
        return jsonify(dict(post)), 200
    except Exception as e:
        return jsonify({"erro": f"Ocorreu um erro: {e}"}), 500

@app.route('/posts/<int:post_id>', methods=['PUT'])
def atualizar_post(post_id):
    """
    Atualiza um post existente.
    Espera um JSON com 'titulo' e/ou 'conteudo'.
    """
    if not request.is_json:
        return jsonify({"erro": "O corpo da requisição deve ser JSON"}), 400
    dados = request.get_json()
    titulo = dados.get('titulo')
    conteudo = dados.get('conteudo')
    if not titulo and not conteudo:
        return jsonify({"erro": "Título ou conteúdo são obrigatórios para a atualização"}), 400
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
        post = cursor.fetchone()
        if post is None:
            conn.close()
            return jsonify({"erro": "Post não encontrado"}), 404
        updates = []
        params = []
        if titulo:
            updates.append("titulo = ?")
            params.append(titulo)
        if conteudo:
            updates.append("conteudo = ?")
            params.append(conteudo)
        params.append(post_id)
        query = "UPDATE posts SET " + ", ".join(updates) + " WHERE id = ?"
        cursor.execute(query, tuple(params))
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Post atualizado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"erro": f"Ocorreu um erro: {e}"}), 500

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def deletar_post(post_id):
    """
    Deleta um post pelo seu ID.
    """
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        rows_affected = cursor.rowcount
        conn.commit()
        conn.close()
        if rows_affected == 0:
            return jsonify({"erro": "Post não encontrado"}), 404
        return jsonify({"mensagem": "Post deletado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"erro": f"Ocorreu um erro: {e}"}), 500

# 4. Bloco condicional para rodar o servidor
if __name__ == '__main__':
    app.run(debug=True)