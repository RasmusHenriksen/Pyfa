# disintegratorWeaponDamageMultiply
#
# Used by:
# Modules from group: Entropic Radiation Sink (4 of 4)
type = "passive"


def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Precursor Weapon",
                                     "damageMultiplier", module.getModifiedItemAttr("damageMultiplier"),
                                     stackingPenalties=True)
