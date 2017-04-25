

namespace Data
{
    /// <summary>
    /// 类描述
    /// </summary>
    public class EnemyInfo
    {
	
        /// <summary>
        /// ID
        /// </summary>
        public int id;
        /// <summary>
        /// 名称
        /// </summary>
        public string name;
        /// <summary>
        /// 预制体
        /// </summary>
        public string prefab;
        /// <summary>
        /// 血量
        /// </summary>
        public float hp;
        /// <summary>
        /// 破损装备血量(多个以^分割)
        /// </summary>
        public string hpBreak;
        /// <summary>
        /// 移动速度
        /// </summary>
        public float speed;
        /// <summary>
        /// 攻击力
        /// </summary>
        public float attackValue;
        /// <summary>
        /// 攻击间隔
        /// </summary>
        public float attackTimeSpan;
        /// <summary>
        /// 攻击距离
        /// </summary>
        public float attackLength;
        /// <summary>
        /// 描述
        /// </summary>
        public string describe;
    }
}
