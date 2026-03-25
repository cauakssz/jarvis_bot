import discord
from discord.ext import commands
import json

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix=".",
    intents=intents
)

# guardar quem já iniciou cadastro
usuarios_cadastro = {}

@bot.event
async def on_ready():
    print(f"✅ {bot.user} está online!")

# boas-vindas ao entrar no servidor, uma maneira amigável de receber novos membros e incentivá-los a interagir com o bot desde o início. Pode ser expandido para incluir mais informações ou links úteis.
@bot.event
async def on_member_join(member):
    try:
        await member.send(
            f"👋 Olá, {member.name}!\n\n"
            "Eu sou o Jarvis 🤖\n"
            "Use `.ajuda` ou diga 'hey jarvis'"
        )
    except:
        print("Erro ao enviar DM")

# mensagens gerais 
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    conteudo = message.content.lower()

    # chamar o bot de forma natural, uma maneira de tornar a interação mais fluida e menos dependente de comandos específicos.
    if "hey jarvis" in conteudo:
        await message.channel.send("👀 Estou aqui! Use `.ajuda`")

    # respostas automáticas
    if "regras" in conteudo:
        await message.channel.send("📜 Veja as regras no canal #regras")

    if "ajuda" in conteudo:
        await message.channel.send("Use `.ajuda` para ver comandos")

    # anti-spam simples que pode ser expandido para algo mais robusto, mas já é um passo para evitar que o servidor seja inundado com links indesejados.
    if conteudo.count("http") > 2:
        await message.delete()
        await message.channel.send("🚫 Evite spam de links!")

    await bot.process_commands(message)

# log de mensagens apagadas
@bot.event
async def on_message_delete(message):
    print(f"{message.author} apagou: {message.content}")

# comando básico para comprimentar :)
@bot.command()
async def ola(ctx):
    await ctx.reply(f"Olá, {ctx.author.name}! 👋")

# mostra aos usuários os comandos disponíveis, além de ser uma boa prática para ajudar novos membros a entenderem o que o bot pode fazer. Pode ser expandido com mais detalhes ou categorias de comandos.
@bot.command()
async def ajuda(ctx):
    embed = discord.Embed(
        title="📋 Central de Comandos - Jarvis 🤖",
        description="Aqui estão algumas coisas que posso fazer:",
        color=discord.Color.purple()
    )

    embed.add_field(
        name="👋 Básicos",
        value="`.ola`\n`.conhecer`",
        inline=False
    )

    embed.add_field(
        name="🛡️ Moderação",
        value="`.limpar 5`",
        inline=False
    )

    embed.add_field(
        name="📝 Sistema",
        value="`.cadastro`",
        inline=False
    )

    embed.set_footer(text="Diga: hey jarvis")

    await ctx.send(embed=embed)

# moderação básica, visando mostrar que o bot pode ser útil para manter a organização do servidor, além de ser um exemplo simples de comando com permissão.
@bot.command()
@commands.has_permissions(manage_messages=True)
async def limpar(ctx, quantidade: int):
    await ctx.channel.purge(limit=quantidade)
    await ctx.send(f"🧹 {quantidade} mensagens apagadas.", delete_after=3)

# mini formulário, uma boa alternativa para coletar informações em determinados tipos de servidores. Pode ser expandido mais ainda pórem ainda é um exemplo simples, mas já é um passo para algo mais complexo como um sistema de tickets ou formulários personalizados.
@bot.command()
async def cadastro(ctx):
    await ctx.send("📋 Vamos começar!\nQual é seu nome?")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        nome = await bot.wait_for("message", timeout=60.0, check=check)

        await ctx.send("Qual sua data de nascimento?")
        idade = await bot.wait_for("message", timeout=60.0, check=check)

        # carregar dados existentes
        try:
            with open("cadastros.json", "r") as arquivo:
                dados = json.load(arquivo)
        except:
            dados = {}

        # salvar novo cadastro
        dados[str(ctx.author.id)] = {
            "nome": nome.content,
            "idade": idade.content
        }

        # salvar no arquivo json
        with open("cadastros.json", "w") as arquivo:
            json.dump(dados, arquivo, indent=4)

        await ctx.send("✅ Cadastro concluído!")
        await ctx.send(f"📌 Nome: {nome.content} | Data de Nascimento: {idade.content}")

    except:
        await ctx.send("⏰ Tempo esgotado, tente novamente.")

# comando para conhecer o criador, uma maneira de criar uma conexão mais pessoal com os usuários, mostrando quem está por trás do bot.
@bot.command()
async def conhecer(ctx):
    embed = discord.Embed(
        title="✨ Conheça quem me criou!",
        description=(
            "Eu fui desenvolvido com dedicação para ajudar pessoas 🤖\n\n"
            "*Conheça mais da pessoa que me fez estar aqui te ajudando!*"
        ),
        color=discord.Color.purple()
    )

    embed.add_field(
        name="🔗 GitHub",
        value="https://github.com/cauakssz",
        inline=False
    )

    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text="Jarvis • Seu assistente virtual")

    await ctx.send(embed=embed)

bot.run("SEU_TOKEN_AQUI ")