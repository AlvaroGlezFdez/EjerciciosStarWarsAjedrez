


#Hacemos los imports de las naves y de la estrella de la muerte al main
from EstrellaDeLaMuerte import EstrellaDeLaMuerte
from naves_aliadas import Nave_Aliada_pequeña, Nave_Aliada_Grande

# Crear instancias de la Estrella de la Muerte y naves aliadas
estrella_muerte = EstrellaDeLaMuerte()
nave_pequena = Nave_Aliada_pequeña("Nave Pequeña", 150)
nave_grande =  Nave_Aliada_Grande ("Nave Grande", 800)

#  comandos para atacar naves aliadas desde la Estrella de la Muerte
estrella_muerte.atacar_nave_aliada(nave_pequena)
estrella_muerte.atacar_nave_aliada(nave_grande)