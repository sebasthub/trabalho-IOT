# Tranca de porta por qr code
##esse projeto teve o intuito de criar uma trava de porta que sera aberta por um qr code gerado por um aplicativo para a disciplina de IOT da catolica
<h3>partes necessarias</h3>
<ul>
  <li>Webcam usb</li>
  <li>Protoboard 830 pontos</li>
  <li>Resistor de carbono</li>
  <li>Led verde</li>
  <li>Push Button</li>
  <li>Motor de passo 28BYJ-48</li>
  <li>rapiberry py 3b</li>
</ul>
<h3>esquematica do projeto</h3>
<p>lembrando que a camera usb deve estar conectada</p>
<a href="https://ibb.co/6wG10sy"><img src="https://i.ibb.co/kBz92cG/tranca-de-porta-por-qr-code-bb.png" alt="tranca-de-porta-por-qr-code-bb" border="0"></a>
<h3>imagem do projeto real</h3>
<a href="https://ibb.co/TYLP5rb"><img src="https://i.ibb.co/PFQ18t9/Whats-App-Image-2023-11-30-at-22-35-58-be785807.jpg" alt="Whats-App-Image-2023-11-30-at-22-35-58-be785807" border="0"></a>
<h3>video de funcionamento</h3>
<a href="https://youtube.com/shorts/Ty124AR1RW8?si=NJAoZCAlO6ySmaT2"><img src="https://www.shareicon.net/data/2015/09/04/95565_yt_512x512.png"/></a>
<h3>comandos para rodar</h3>
<h4>rode os comandos na rapiberry py 3b</h4>
<h5>comando para clonar o repo</h5>
<code>git clone https://github.com/sebasthub/tranca-de-porta-por-qr.git</code>
<h5>acesse o repositorio</h5>
<code>cd ./tranca-de-porta-por-qr</code>
<h5>baixe as bibliotecas</h5>
<code>pip install -r requirements.txt</code>
<h5>agora rode o codigo</h5>
<code>python3 ./logica.py</code>
