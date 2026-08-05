// Helper para Fallback de imagens de gastronomia em alta definição (Unsplash HD) com palavras-chave específicas do prato
function getGastronomyImageFallback(title, id) {
    const t = (title || '').toLowerCase();
    const fallbacks = {
        salmon: [
            'https://images.unsplash.com/photo-1467003909585-2f8a72700288?auto=format&fit=crop&w=800&q=80',
            'https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=800&q=80'
        ],
        hake_fish: [
            'https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=800&q=80',
            'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80',
            'https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=800&q=80'
        ],
        chicken: [
            'https://images.unsplash.com/photo-1604908554025-aaa87c152c7b?auto=format&fit=crop&w=800&q=80',
            'https://images.unsplash.com/photo-1532550907401-a500c9a57435?auto=format&fit=crop&w=800&q=80'
        ],
        beef: [
            'https://images.unsplash.com/photo-1543339308-43e59d6b73a6?auto=format&fit=crop&w=800&q=80',
            'https://images.unsplash.com/photo-1558030006-450675393462?auto=format&fit=crop&w=800&q=80'
        ],
        pancake: [
            'https://images.unsplash.com/photo-1528207776546-365bb710ee93?auto=format&fit=crop&w=800&q=80',
            'https://images.unsplash.com/photo-1506084868230-bb9d95c24759?auto=format&fit=crop&w=800&q=80',
            'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?auto=format&fit=crop&w=800&q=80'
        ],
        omelette: [
            'https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=800&q=80',
            'https://images.unsplash.com/photo-1510693206972-df098062cb71?auto=format&fit=crop&w=800&q=80'
        ],
        porridge: [
            'https://images.unsplash.com/photo-1517673132405-a56a62b18caf?auto=format&fit=crop&w=800&q=80',
            'https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=800&q=80'
        ],
        salad: [
            'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80',
            'https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80',
            'https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=800&q=80'
        ],
        dessert_protein: [
            'https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=format&fit=crop&w=800&q=80',
            'https://images.unsplash.com/photo-1494597564530-871f2b93ac55?auto=format&fit=crop&w=800&q=80',
            'https://images.unsplash.com/photo-1505252585461-04db1eb84625?auto=format&fit=crop&w=800&q=80'
        ]
    };

    if (t.includes('salmón') || t.includes('salmon') || t.includes('atún') || t.includes('atun')) {
        return fallbacks.salmon[id % fallbacks.salmon.length];
    } else if (t.includes('merluza') || t.includes('lubina') || t.includes('dorada') || t.includes('pescado') || t.includes('marisco') || t.includes('sepia') || t.includes('gambas') || t.includes('pulpo') || t.includes('hake')) {
        return fallbacks.hake_fish[id % fallbacks.hake_fish.length];
    } else if (t.includes('pollo') || t.includes('pechuga') || t.includes('pavo') || t.includes('chicken')) {
        return fallbacks.chicken[id % fallbacks.chicken.length];
    } else if (t.includes('ternera') || t.includes('lomo') || t.includes('carne') || t.includes('beef') || t.includes('solomillo')) {
        return fallbacks.beef[id % fallbacks.beef.length];
    } else if (t.includes('tortita') || t.includes('panqueque') || t.includes('crepa') || t.includes('crepe') || t.includes('gofre') || t.includes('waffle') || t.includes('pancake')) {
        return fallbacks.pancake[id % fallbacks.pancake.length];
    } else if (t.includes('huevo') || t.includes('tortilla') || t.includes('revuelto') || t.includes('shakshuka') || t.includes('omelette')) {
        return fallbacks.omelette[id % fallbacks.omelette.length];
    } else if (t.includes('avena') || t.includes('porridge') || t.includes('gachas') || t.includes('cereal') || t.includes('bol')) {
        return fallbacks.porridge[id % fallbacks.porridge.length];
    } else if (t.includes('ensalada') || t.includes('quinoa') || t.includes('verdura') || t.includes('garbanzo') || t.includes('lenteja') || t.includes('boniato')) {
        return fallbacks.salad[id % fallbacks.salad.length];
    } else {
        return fallbacks.dessert_protein[id % fallbacks.dessert_protein.length];
    }
}

// Função para atualizar a visualização em tempo real
function updatePreview() {
    document.getElementById('preview-title').innerHTML = document.getElementById('input-title').value.replace(/\n/g, '<br>');
    document.getElementById('preview-subtitle').innerText = document.getElementById('input-subtitle').value;
    document.getElementById('preview-time').innerText = document.getElementById('input-time').value;
    document.getElementById('preview-yield').innerText = document.getElementById('input-yield').value;
    
    // Atualizar imagem com fallback inteligente de gastronomia HD
    const imgInput = document.getElementById('input-image').value.trim();
    const previewImg = document.getElementById('preview-image');
    const titleVal = document.getElementById('input-title').value;
    const recipeId = parseInt(document.getElementById('recipe-selector')?.value) || 1;
    const fallbackUrl = getGastronomyImageFallback(titleVal, recipeId);

    if (imgInput && (imgInput.startsWith('http://') || imgInput.startsWith('https://') || imgInput.startsWith('data:image'))) {
        previewImg.src = imgInput;
    } else {
        previewImg.src = fallbackUrl;
    }

    // Tratamento extra caso falhe o carregamento da imagem
    previewImg.onerror = function() {
        this.onerror = null;
        this.src = fallbackUrl;
    };
    
    // Ingredientes
    const ingText = document.getElementById('input-ingredients').value;
    const ingLines = ingText.split('\n').filter(line => line.trim() !== '');
    const ingHtml = ingLines.map(line => `<li>${line}</li>`).join('');
    document.getElementById('preview-ingredients').innerHTML = ingHtml;

    // Instruções (Garantir 5 a 8 passos bem detalhados)
    const instText = document.getElementById('input-instructions').value;
    let instLines = instText.split('\n').filter(line => line.trim() !== '');
    if (instLines.length < 5) {
        if (!instLines.some(l => l.toLowerCase().includes('emplatado') || l.toLowerCase().includes('servir'))) {
            instLines.push("Verifique el punto exacto de cocción para mantener la textura tierna y la máxima jugosidad natural.");
            instLines.push("Emplatado Editorial: Sirva en un plato de cerámica templado y decore con hierbas frescas o especias aromáticas.");
        }
    }
    const instHtml = instLines.map(line => `<li>${line}</li>`).join('');
    document.getElementById('preview-instructions').innerHTML = instHtml;

    // Variações e Dicas Gourmet do Chef
    const varText = document.getElementById('input-variations').value;
    let varLines = varText.split('\n').filter(line => line.trim() !== '');
    if (varLines.length === 0 || varLines.length < 2) {
        varLines.push("👨‍🍳 Consejo del Chef: Controlar la temperatura del fuego para preservar todas las vitaminas y propiedades organolépticas.");
        varLines.push("🌿 Toque Mediterráneo: Puedes incorporar unas gotas de aceite de oliva virgen extra en crudo al momento de servir.");
    }
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

// Função para carregar as 140 receitas no dropdown
function initRecipeSelector() {
    const selector = document.getElementById('recipe-selector');
    if (!selector || selector.options.length > 1 || !window.RECETAS_140_DATA) return;

    const allRecipes = [
        ...(window.RECETAS_140_DATA.parte1 || []),
        ...(window.RECETAS_140_DATA.parte2 || [])
    ];
    allRecipes.forEach(rec => {
        const opt = document.createElement('option');
        opt.value = rec.id;
        opt.innerText = `#${rec.id} - ${rec.titulo} (${rec.capitulo})`;
        selector.appendChild(opt);
    });

    selector.addEventListener('change', () => {
        const selectedId = parseInt(selector.value);
        if (!selectedId) return;
        const rec = allRecipes.find(r => r.id === selectedId);
        if (rec) {
            document.getElementById('input-title').value = rec.titulo;
            document.getElementById('input-subtitle').value = rec.frase_efecto;
            document.getElementById('input-time').value = rec.tiempo;
            document.getElementById('input-yield').value = rec.rendimiento;
            const bestImgUrl = (rec.foto_arquivo && (rec.foto_arquivo.startsWith('http://') || rec.foto_arquivo.startsWith('https://')))
                ? rec.foto_arquivo
                : getGastronomyImageFallback(rec.titulo, rec.id);
            document.getElementById('input-image').value = bestImgUrl;
            document.getElementById('input-ingredients').value = (rec.ingredientes || []).join('\n');
            document.getElementById('input-instructions').value = (rec.modo_preparo || []).join('\n');
            document.getElementById('input-variations').value = (rec.variaciones || []).join('\n');
            document.getElementById('input-note').value = rec.frase_lateral || '';
            document.getElementById('input-target').value = rec.objetivo_titulo || '';
            document.getElementById('input-target-comment').value = rec.objetivo_descripcion || '';
            if (rec.macros) {
                document.getElementById('input-cal').value = rec.macros.calorias || '';
                document.getElementById('input-prot').value = rec.macros.proteinas || '';
                document.getElementById('input-carb').value = rec.macros.carbohidratos || '';
                document.getElementById('input-fat').value = rec.macros.grasas || '';
                document.getElementById('input-fib').value = rec.macros.fibra || '';
            }
            updatePreview();
        }
    });
}

// Inicializa de imediato e também em eventos de carregamento
initRecipeSelector();
window.addEventListener('DOMContentLoaded', initRecipeSelector);
window.addEventListener('load', initRecipeSelector);
setTimeout(initRecipeSelector, 500);


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
