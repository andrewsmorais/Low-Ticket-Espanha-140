// Função para atualizar a visualização em tempo real
function updatePreview() {
    document.getElementById('preview-title').innerHTML = document.getElementById('input-title').value.replace(/\n/g, '<br>');
    document.getElementById('preview-subtitle').innerText = document.getElementById('input-subtitle').value;
    document.getElementById('preview-time').innerText = document.getElementById('input-time').value;
    document.getElementById('preview-yield').innerText = document.getElementById('input-yield').value;
    
    // Atualizar imagem (pode ser link da web ou caminho local se estiver na mesma pasta)
    const imgUrl = document.getElementById('input-image').value;
    if(imgUrl) {
        document.getElementById('preview-image').src = imgUrl;
    }
    
    // Ingredientes
    const ingText = document.getElementById('input-ingredients').value;
    const ingLines = ingText.split('\n').filter(line => line.trim() !== '');
    const ingHtml = ingLines.map(line => `<li>${line}</li>`).join('');
    document.getElementById('preview-ingredients').innerHTML = ingHtml;

    // Instruções
    const instText = document.getElementById('input-instructions').value;
    const instLines = instText.split('\n').filter(line => line.trim() !== '');
    const instHtml = instLines.map(line => `<li>${line}</li>`).join('');
    document.getElementById('preview-instructions').innerHTML = instHtml;

    // Variações
    const varText = document.getElementById('input-variations').value;
    const varLines = varText.split('\n').filter(line => line.trim() !== '');
    const varHtml = varLines.map(line => `<li>${line}</li>`).join('');
    document.getElementById('preview-variations').innerHTML = varHtml;

    // Nota / Dica
    document.getElementById('preview-note').innerText = document.getElementById('input-note').value;

    // Objetivo / Foco
    document.getElementById('preview-target').innerText = document.getElementById('input-target').value;
    document.getElementById('preview-target-comment').innerText = document.getElementById('input-target-comment').value;

    // Tabela Nutricional
    document.getElementById('preview-cal').innerText = document.getElementById('input-cal').value;
    document.getElementById('preview-prot').innerText = document.getElementById('input-prot').value;
    document.getElementById('preview-carb').innerText = document.getElementById('input-carb').value;
    document.getElementById('preview-fat').innerText = document.getElementById('input-fat').value;
    document.getElementById('preview-fib').innerText = document.getElementById('input-fib').value;
}

// Adicionar eventos para atualizar ao digitar
const inputs = document.querySelectorAll('input, textarea');
inputs.forEach(input => {
    input.addEventListener('input', updatePreview);
});

// Atualizar logo que abre
updatePreview();

// Função para baixar como Imagem PNG
function downloadImage() {
    const recipeCard = document.getElementById('recipe-card');
    
    // Mostra um aviso pro usuário
    const btn = document.querySelector('.btn-download');
    const originalText = btn.innerText;
    btn.innerText = '⏳ Gerando imagem...';
    
    html2canvas(recipeCard, {
        scale: 2, // Maior resolução
        useCORS: true,
        backgroundColor: '#faf5eb'
    }).then(canvas => {
        const link = document.createElement('a');
        link.download = 'minha-receita.png';
        link.href = canvas.toDataURL('image/png');
        link.click();
        
        btn.innerText = originalText;
    }).catch(err => {
        console.error(err);
        alert("Ocorreu um erro ao gerar a imagem. Se usou imagem da web, tente salvar a imagem na pasta do projeto e usar o nome dela (ex: foto.jpg).");
        btn.innerText = originalText;
    });
}

// Função para baixar como PDF (ideal para Ebooks)
function downloadPDF() {
    const recipeCard = document.getElementById('recipe-card');
    const btn = document.querySelector('.btn-download.pdf');
    const originalText = btn.innerText;
    btn.innerText = '⏳ Gerando PDF...';
    
    html2canvas(recipeCard, {
        scale: 2,
        useCORS: true,
        backgroundColor: '#faf5eb'
    }).then(canvas => {
        const imgData = canvas.toDataURL('image/png');
        
        // Inicializa o jsPDF (A4 portrait)
        const { jsPDF } = window.jspdf;
        const pdf = new jsPDF('p', 'mm', 'a4');
        
        const pdfWidth = pdf.internal.pageSize.getWidth();
        const pdfHeight = (canvas.height * pdfWidth) / canvas.width;
        
        pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
        pdf.save('minha-receita.pdf');
        
        btn.innerText = originalText;
    }).catch(err => {
        console.error(err);
        alert("Ocorreu um erro ao gerar o PDF.");
        btn.innerText = originalText;
    });
}
