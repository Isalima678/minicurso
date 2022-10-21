--create table cd (codigocd integer primary key, titulo varchar(30), datacompra date, localcompra varchar(30), valorpago decimal(5,2));
-- table musica(codigomusica integer primary key, codigocd integer, nomemusica varchar(30), artista varchar(40), tempomusica time, foreign key (codigocd) references cd);
select * from cd;
Select cd.titulo,musica.nomemusica, musica.artista from cd, musica where cd.codigocd=musica.codigocd;
select sum(valorpago) as TotalPagoCD from cd;
select * from musica where codigocd=1;
select codigomusica,nomemusica, artista from musica;
select sum(tempomusica) as TempoTotal, musica.codigocd as CD from musica group by musica.codigocd
select count(*) as QuantidadeMusicas from musica;
select avg(tempomusica),musica.codigocd from musica group by musica.codigocd;
select count(nomemusica)as quantidademusicas, codigocd from musica group by codigocd
select count(nomemusica)as QtdadeMusicas from musica where artista like 'Ivete Sangalo';
select * from cd where localcompra like 'Centro'
select Max(valorpago) as CDmaisCaro from cd;

